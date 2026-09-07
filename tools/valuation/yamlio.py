"""The one writer for ``assumptions.yaml`` (AGENTS.md section 18.9, section 18.10).

Everything that changes a YAML file on disk goes through this module.  It uses
``ruamel.yaml`` in round-trip mode so hand-written comments, key order, block
scalars (the stories), flow-style cells and quoting survive a save.  The engine's
read path stays on PyYAML (:func:`valuation.schema.load_yaml`); the plain dict it
reads must always equal ``yaml.safe_load`` of what this module writes.

Typical use (the app's Save button)::

    doc = yamlio.load_roundtrip(path)                 # data + snapshot of the file
    changed = yamlio.apply_changes(doc, [("scenarios.base.sales_to_capital.value", 2.0)])
    yamlio.append_changelog(doc, [{"at": ts, "path": p, "old": o, "new": n, "note": note}
                                  for p, o, n in changed])
    yamlio.set_owner_edited(doc, ts)
    yamlio.save(doc)                                  # atomic; refuses if the file changed since load
"""

from __future__ import annotations

import hashlib
import io
import math
import os
import tempfile
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any, Iterable

import yaml
from ruamel.yaml import YAML
from ruamel.yaml.comments import CommentedMap, CommentedSeq
from ruamel.yaml.scalarstring import DoubleQuotedScalarString, LiteralScalarString

from .schema import split_path

ABSENT = "<absent>"          # shown in diffs when one side has no such key


class StaleFileError(Exception):
    """The file on disk changed after it was loaded; the caller must reload before saving."""


class PathError(Exception):
    """A dotted path does not resolve inside the document."""


@dataclass
class Snapshot:
    """What the file looked like when it was loaded: enough to detect a change."""
    mtime_ns: int
    digest: str

    @classmethod
    def of(cls, path: Path) -> "Snapshot":
        data = path.read_bytes()
        return cls(mtime_ns=path.stat().st_mtime_ns, digest=hashlib.sha256(data).hexdigest())

    def matches(self, path: Path) -> bool:
        if not path.exists():
            return False
        if path.stat().st_mtime_ns == self.mtime_ns:
            return True
        return hashlib.sha256(path.read_bytes()).hexdigest() == self.digest


@dataclass
class Document:
    """A round-trip loaded YAML document plus the snapshot of the file it came from."""
    data: CommentedMap
    path: Path
    snapshot: Snapshot

    def plain(self) -> dict[str, Any]:
        """The plain Python dict the engine would read from this document as saved."""
        return to_plain(self.data)


@dataclass
class Change:
    path: str
    file_value: Any
    current_value: Any


# --------------------------------------------------------------------------- #
# ruamel configuration
# --------------------------------------------------------------------------- #

def _represent_none(representer, data):                     # noqa: ANN001 - ruamel hook
    return representer.represent_scalar("tag:yaml.org,2002:null", "null")


def _yaml() -> YAML:
    y = YAML()                                              # round-trip mode
    y.preserve_quotes = True
    y.width = 1_000_000                                     # never re-wrap long reasons
    y.indent(mapping=2, sequence=4, offset=2)               # the layout the analysts use
    y.representer.add_representer(type(None), _represent_none)
    return y


def dumps(data: CommentedMap) -> str:
    buf = io.StringIO()
    _yaml().dump(data, buf)
    return buf.getvalue()


def to_plain(data: Any) -> Any:
    """Convert a ruamel structure into plain dicts, lists and scalars (what PyYAML would read)."""
    return yaml.safe_load(dumps(data)) if isinstance(data, (CommentedMap, CommentedSeq)) else data


# --------------------------------------------------------------------------- #
# Load / save
# --------------------------------------------------------------------------- #

def load_roundtrip(path: str | Path) -> Document:
    path = Path(path).resolve()
    text = path.read_text(encoding="utf-8")
    data = _yaml().load(text)
    if not isinstance(data, CommentedMap):
        raise ValueError(f"{path}: top level must be a mapping")
    return Document(data=data, path=path, snapshot=Snapshot.of(path))


def save(doc: Document, path: str | Path | None = None, *, snapshot: Snapshot | None = None) -> Snapshot:
    """Write atomically (temp file in the same directory, then rename).

    Refuses with :class:`StaleFileError` when the target file changed since ``snapshot``
    (default: the snapshot taken at load).  Saving to a new path never trips the guard.
    Returns the snapshot of the written file and stores it on ``doc``.
    """
    target = Path(path).resolve() if path is not None else doc.path
    guard = snapshot or doc.snapshot
    if target == doc.path and target.exists() and not guard.matches(target):
        raise StaleFileError(
            f"{target} changed on disk after it was loaded (another process or an agent wrote it). "
            "Reload the file and apply the changes again before saving.")
    text = dumps(doc.data)
    target.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp_name = tempfile.mkstemp(prefix=".assumptions-", suffix=".yaml.tmp", dir=str(target.parent))
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as fh:
            fh.write(text)
            fh.flush()
            os.fsync(fh.fileno())
        os.replace(tmp_name, target)
    except BaseException:
        try:
            os.unlink(tmp_name)
        except OSError:
            pass
        raise
    doc.path = target
    doc.snapshot = Snapshot.of(target)
    return doc.snapshot


# --------------------------------------------------------------------------- #
# Editing
# --------------------------------------------------------------------------- #

def _walk(node: Any, parts: list[str | int], path: str) -> Any:
    for part in parts:
        if isinstance(node, (list, CommentedSeq)):
            if not isinstance(part, int) or part >= len(node):
                raise PathError(f"{path}: list index {part!r} out of range")
            node = node[part]
        elif isinstance(node, (dict, CommentedMap)):
            if part not in node:
                raise PathError(f"{path}: key {part!r} not found")
            node = node[part]
        else:
            raise PathError(f"{path}: {part!r} is below a scalar")
    return node


def _wrap(old: Any, new: Any) -> Any:
    """Keep the file's scalar style where it matters: multi-line strings stay block scalars."""
    if isinstance(new, str):
        if isinstance(old, LiteralScalarString) or "\n" in new:
            text = new if new.endswith("\n") else new + "\n"
            return LiteralScalarString(text)
        return new
    if isinstance(new, float) and (math.isnan(new) or math.isinf(new)):
        raise ValueError("NaN and infinity cannot be written into assumptions.yaml")
    if isinstance(new, bool) or new is None or isinstance(new, (int, float)):
        return new
    if isinstance(new, dict):
        m = CommentedMap()
        for k, v in new.items():
            m[k] = _wrap(None, v)
        return m
    if isinstance(new, (list, tuple)):
        s = CommentedSeq()
        for v in new:
            s.append(_wrap(None, v))
        if all(v is None or isinstance(v, (int, float, str, bool)) for v in new):
            s.fa.set_flow_style()                           # per-year lists stay on one line
        return s
    return new


def apply_changes(doc: Document | CommentedMap, changes: Iterable[tuple[str, Any]]) -> list[tuple[str, Any, Any]]:
    """Set every ``(dotted_path, new_value)`` in place.

    List indices are allowed (``scenarios.base.operating_margin.values.4``).  Missing
    intermediate mappings are created; a missing final key is added at the end of its
    mapping.  Returns ``[(path, old_plain_value, new_plain_value), ...]`` for the entries
    whose value actually changed.
    """
    data = doc.data if isinstance(doc, Document) else doc
    changed: list[tuple[str, Any, Any]] = []
    for path, value in changes:
        parts = split_path(path)
        if not parts:
            raise PathError("empty path")
        parent: Any = data
        for i, part in enumerate(parts[:-1]):
            nxt = parts[i + 1]
            if isinstance(parent, (list, CommentedSeq)):
                if not isinstance(part, int) or part >= len(parent):
                    raise PathError(f"{path}: list index {part!r} out of range")
                if parent[part] is None:
                    parent[part] = CommentedSeq() if isinstance(nxt, int) else CommentedMap()
                parent = parent[part]
            elif isinstance(parent, (dict, CommentedMap)):
                if part not in parent or parent[part] is None:
                    if isinstance(nxt, int):
                        raise PathError(f"{path}: cannot create a list at {part!r}; list indices must exist")
                    parent[part] = CommentedMap()
                parent = parent[part]
            else:
                raise PathError(f"{path}: {part!r} is below a scalar")
        last = parts[-1]
        if isinstance(parent, (list, CommentedSeq)):
            if not isinstance(last, int) or last >= len(parent):
                raise PathError(f"{path}: list index {last!r} out of range")
            old = parent[last]
        elif isinstance(parent, (dict, CommentedMap)):
            old = parent.get(last)
        else:
            raise PathError(f"{path}: cannot set a key on a scalar")
        old_plain = to_plain(old) if isinstance(old, (CommentedMap, CommentedSeq)) else _scalar_plain(old)
        new_plain = _scalar_plain(value) if not isinstance(value, (dict, list, tuple)) else value
        if _same(old_plain, new_plain):
            continue
        parent[last] = _wrap(old, value)
        changed.append((path, old_plain, new_plain))
    return changed


def _scalar_plain(x: Any) -> Any:
    """ruamel scalars (ScalarFloat, LiteralScalarString, ...) as plain Python values."""
    if x is None or isinstance(x, bool):
        return x
    if isinstance(x, str):
        return str(x)
    if isinstance(x, int):
        return int(x)
    if isinstance(x, float):
        return float(x)
    if isinstance(x, (datetime,)):
        return x
    return x


def _same(a: Any, b: Any) -> bool:
    if isinstance(a, bool) or isinstance(b, bool):
        return a is b
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return math.isclose(float(a), float(b), rel_tol=0.0, abs_tol=1e-12)
    return a == b


def append_changelog(doc: Document | CommentedMap, entries: Iterable[dict[str, Any]]) -> int:
    """Append ``{at, path, old, new, note}`` entries to ``changelog`` (created if absent, oldest first)."""
    data = doc.data if isinstance(doc, Document) else doc
    entries = list(entries)
    if not entries:
        return 0
    log = data.get("changelog")
    if not isinstance(log, CommentedSeq):
        log = CommentedSeq()
        data["changelog"] = log
    for entry in entries:
        item = CommentedMap()
        item["at"] = DoubleQuotedScalarString(str(entry.get("at") or _now_iso()))
        item["path"] = str(entry["path"])
        item["old"] = _wrap(None, entry.get("old"))
        item["new"] = _wrap(None, entry.get("new"))
        note = entry.get("note")
        item["note"] = DoubleQuotedScalarString(str(note)) if note else None
        item.fa.set_flow_style()
        log.append(item)
    return len(entries)


def set_owner_edited(doc: Document | CommentedMap, iso_timestamp: str | None = None) -> str:
    """Set the top-level ``owner_edited`` stamp (placed just before ``changelog`` when that exists)."""
    data = doc.data if isinstance(doc, Document) else doc
    stamp = DoubleQuotedScalarString(iso_timestamp or _now_iso())
    if "owner_edited" in data:
        data["owner_edited"] = stamp
    elif "changelog" in data:
        keys = list(data.keys())
        data.insert(keys.index("changelog"), "owner_edited", stamp)
    else:
        data["owner_edited"] = stamp
    return str(stamp)


def _now_iso() -> str:
    return datetime.now().replace(microsecond=0).isoformat()


# --------------------------------------------------------------------------- #
# Diff
# --------------------------------------------------------------------------- #

def _strip_private(d: Any) -> Any:
    if isinstance(d, dict):
        return {k: v for k, v in d.items() if not (isinstance(k, str) and k.startswith("_"))}
    return d


def diff_plain(file_value: Any, current_value: Any, prefix: str = "") -> list[Change]:
    """Dotted-path differences between two plain structures (list indices included)."""
    out: list[Change] = []
    if isinstance(file_value, dict) and isinstance(current_value, dict):
        keys = list(file_value.keys()) + [k for k in current_value.keys() if k not in file_value]
        for k in keys:
            p = f"{prefix}.{k}" if prefix else str(k)
            if k not in file_value:
                out.append(Change(p, ABSENT, current_value[k]))
            elif k not in current_value:
                out.append(Change(p, file_value[k], ABSENT))
            else:
                out.extend(diff_plain(file_value[k], current_value[k], p))
        return out
    if isinstance(file_value, list) and isinstance(current_value, list):
        if len(file_value) != len(current_value):
            out.append(Change(prefix, file_value, current_value))
            return out
        for i, (a, b) in enumerate(zip(file_value, current_value)):
            out.extend(diff_plain(a, b, f"{prefix}.{i}" if prefix else str(i)))
        return out
    if not _same(file_value, current_value):
        out.append(Change(prefix, file_value, current_value))
    return out


def diff_against_file(path: str | Path, current_plain_dict: dict[str, Any]) -> list[Change]:
    """Changed paths between the YAML on disk and ``current_plain_dict`` (``_path`` ignored)."""
    with open(path, encoding="utf-8") as fh:
        on_disk = yaml.safe_load(fh) or {}
    return diff_plain(_strip_private(on_disk), _strip_private(current_plain_dict))


def changes_from_diff(diff: Iterable[Change]) -> list[tuple[str, Any]]:
    """Turn a diff into ``apply_changes`` input; keys removed in the working copy are set to null."""
    out: list[tuple[str, Any]] = []
    for c in diff:
        out.append((c.path, None if c.current_value == ABSENT else c.current_value))
    return out
