"""An article reader for cached Markdown notes; source text stays unchanged."""
from __future__ import annotations

from dataclasses import dataclass
from html import escape
import re
from urllib.parse import unquote, urlsplit


@dataclass(frozen=True)
class NoteSection:
    heading: str
    body: str


def split_note(content: str, fallback_title: str) -> tuple[str, str, list[NoteSection]]:
    """Lift the title and level-two sections, respecting fenced code blocks."""
    title, intro, sections = fallback_title, [], []
    heading, lines, fence = None, [], ""
    for line in content.splitlines():
        marker = re.match(r"^\s{0,3}(`{3,}|~{3,})", line)
        if marker:
            run = marker[1]
            if not fence:
                fence = run
            elif run[0] == fence[0] and len(run) >= len(fence):
                fence = ""
            lines.append(line)
            continue
        if not fence and heading is None and not sections and not any(s.strip() for s in lines):
            first = re.match(r"^#\s+(.+?)\s*#*\s*$", line)
            if first:
                title = first[1]
                continue
        match = re.match(r"^##\s+(.+?)\s*#*\s*$", line) if not fence else None
        if match:
            if heading is None:
                intro = lines
            else:
                sections.append(NoteSection(heading, "\n".join(lines).strip()))
            heading, lines = match[1], []
        else:
            lines.append(line)
    if heading is None:
        intro = lines
    else:
        sections.append(NoteSection(heading, "\n".join(lines).strip()))
    return title, "\n".join(intro).strip(), sections


def readable_tables(text: str) -> str:
    """Split wide pipe tables, repeating their row labels without changing values."""
    lines, output, i, fence = text.splitlines(), [], 0, ""
    while i < len(lines):
        line = lines[i]
        marker = re.match(r"^\s{0,3}(`{3,}|~{3,})", line)
        if marker:
            run = marker[1]
            if not fence:
                fence = run
            elif run[0] == fence[0] and len(run) >= len(fence):
                fence = ""
        if not fence and line.strip().startswith("|"):
            end = i
            while end < len(lines) and lines[end].strip().startswith("|"):
                end += 1
            rows = [re.split(r"(?<!\\)\|", row.strip().strip("|")) for row in lines[i:end]]
            count = len(rows[0])
            if (count > 5 and len(rows) > 1 and all(len(row) == count for row in rows)
                    and all(re.fullmatch(r"\s*:?-{3,}:?\s*", cell) for cell in rows[1])):
                for start in range(1, count, 4):
                    if start > 1:
                        output.extend(["", "_Table continued — same rows, additional columns._", ""])
                    for row in rows:
                        output.append("|" + "|".join([row[0], *row[start:start + 4]]) + "|")
                i = end
                continue
        output.append(line)
        i += 1
    return "\n".join(output)


def note_markdown(text: str, index, source=None) -> str:
    """Link recorded bracket citations without altering existing links or code."""
    protected = re.compile(r"(```[\s\S]*?```|~~~[\s\S]*?~~~|`+[^`\n]*`+|!?\[[^\]\n]*\]\([^\n]*?\))")
    pieces = protected.split(readable_tables(text))
    for i in range(0, len(pieces), 2):
        pieces[i] = re.sub(r"\[[^\[\]\n]+\](?![(:\[])" ,
                           lambda m: index.render(m[0], str), pieces[i])
        pieces[i] = re.sub(r"(?<!\\)\$", r"\\$", pieces[i])
    for i in range(1, len(pieces), 2):
        link = re.fullmatch(r"\[([^\]]*)\]\(([^\s)]+)\)", pieces[i])
        if not link:
            continue
        label, target = link.groups()
        url = urlsplit(target)
        if url.scheme or url.netloc or not url.path:
            continue
        path = (source.path.parent / unquote(url.path)).resolve() if source else None
        recorded = next((s for s in index.sources if s.path == path), None)
        pieces[i] = (f"[{label}]({recorded.cached_url})" if recorded else
                     label + " (not in this company's recorded sources)")
    return "".join(pieces)


def note_label(path) -> str:
    if path.name == "AGENTS.md":
        return "Research guidelines"
    if path.name.upper().startswith("MANIFEST"):
        return "Source record"
    if ".claude" in path.parts or "damodaran-notes" in path.parts:
        return "Methodology note"
    return "Research note"


NOTE_STYLE = """<style>
/* Only loaded on the separate Markdown reader route. */
[data-testid="stMainBlockContainer"] { max-width: 1020px; padding-top: 3rem; }
.st-key-note_article { padding-bottom: 1.5rem; }
.st-key-note_article h1 { font-size: clamp(1.9rem, 3.1vw, 2.65rem) !important;
    line-height: 1.18; font-weight: 550 !important; max-width: 29ch; padding-top: .35rem; }
.st-key-note_article h2 { font-size: 1.42rem !important; font-weight: 600 !important;
    line-height: 1.4; padding-top: 1.65rem; border-top: 1px solid #eaeaf1; margin-top: 1rem; }
.st-key-note_article h3 { font-size: 1.1rem !important; padding-top: .7rem; }
.st-key-note_article [data-testid="stMarkdownContainer"] p,
.st-key-note_article [data-testid="stMarkdownContainer"] li { font-size: 15px; line-height: 1.85; }
.st-key-note_article [data-testid="stMarkdownContainer"] li { margin-bottom: .4rem; }
.st-key-note_article [data-testid="stMarkdownContainer"] a { color: #5155bb; text-underline-offset: 3px; }
.st-key-note_article [data-testid="stMarkdownContainer"] blockquote { margin: 1.25rem 0;
    padding: 1rem 1.25rem; background: #f6f6fd; border-left: 3px solid #898ce2; border-radius: 0 8px 8px 0; }
.st-key-note_article [data-testid="stMarkdownContainer"]:has(table) { overflow-x: auto; }
.st-key-note_article [data-testid="stMarkdownContainer"] table { width: 100%;
    border: 1px solid #e5e5ef; border-radius: 9px; margin: 1rem 0 1.4rem;
    font-size: 13px; font-variant-numeric: tabular-nums; }
.st-key-note_article [data-testid="stMarkdownContainer"] th { background: #f5f5fa; font-weight: 600; color: #505063; }
.st-key-note_article [data-testid="stMarkdownContainer"] th,
.st-key-note_article [data-testid="stMarkdownContainer"] td { padding: .7rem .85rem; min-width: 7rem;
    border-color: #ebebf2; line-height: 1.65; vertical-align: top; }
.st-key-note_article [data-testid="stMarkdownContainer"] tr:nth-child(even) td { background: #fcfcfe; }
.st-key-note_article [data-testid="stMarkdownContainer"] td:first-child { min-width: 11rem; }
.note-kicker { display: flex; align-items: center; gap: .7rem; color: #78788a;
    font-size: 11px; letter-spacing: .06em; text-transform: uppercase; }
.note-badge { color: #5155ac; background: #eeeefa; border: 1px solid #e0e0f4;
    border-radius: 6px; padding: .3rem .55rem; font-weight: 600; }
.note-byline { color: #737385; font-size: 13px; padding: .1rem 0 1rem; }
#note-results { scroll-margin-top: 4rem; }
.note-toc { padding: .2rem .4rem .8rem; }
.note-toc a { display: block; color: #565669 !important; text-decoration: none;
    font-size: 12px; line-height: 1.5; padding: .45rem .55rem; border-radius: 6px; }
.note-toc a:hover { color: #484bc1 !important; background: #eeeefa; }
.note-toc a:focus-visible { outline: 2px solid #575be7; outline-offset: 1px; }
.st-key-note_navigation [data-testid="stTextInput"] { padding: .2rem .4rem .8rem; }
.st-key-note_navigation [data-testid="stCaptionContainer"] { padding: .3rem .65rem; }
.st-key-note_navigation [data-testid="stDownloadButton"],
.st-key-note_navigation [data-testid="stLinkButton"] { margin: .4rem; }
@media (max-width: 1100px) {
    .st-key-note_article [data-testid="stMarkdownContainer"] th,
    .st-key-note_article [data-testid="stMarkdownContainer"] td { min-width: 5rem; padding: .6rem; }
    .st-key-note_article [data-testid="stMarkdownContainer"] td:first-child { min-width: 8rem; }
}
@media (max-width: 640px) {
    [data-testid="stMainBlockContainer"] { padding-top: 2rem; }
    .st-key-note_article h1 { font-size: 1.9rem !important; }
}
</style>"""


def render_note(source, index, content: str, ticker: str, locator: str, quoted: str) -> None:
    import streamlit as st
    from valuation.app_sources import highlighted_excerpt
    from valuation.source_passages import find_passages

    title, intro, sections = split_note(content, source.tag)
    kind = note_label(source.path)
    st.markdown(NOTE_STYLE, unsafe_allow_html=True)
    with st.sidebar.container(key="note_navigation"):
        st.markdown('<div class="workspace-brand"><span>V</span> Research library</div>', unsafe_allow_html=True)
        st.caption(ticker + " / " + kind)
        search = st.text_input("Search this note", placeholder="Find a phrase or number", max_chars=600,
                               key="note_search:" + source.file)
        result = find_passages(content, locator="" if search else locator, quote=search or quoted) if search or locator or quoted else None
        if search:
            label = f"View matching passages ({len(result.matches)})" if result.matches else "No exact matches · View search details"
            st.markdown('<nav class="note-toc" aria-label="Search results"><a href="#note-results" target="_self">'
                        + label + '</a></nav>', unsafe_allow_html=True)
        if sections:
            st.markdown('<div class="nav-group">In this note</div>', unsafe_allow_html=True)
            links = '<a href="#note-title" target="_self">Introduction</a>'
            links += "".join(f'<a href="#note-section-{i}" target="_self">{escape(s.heading)}</a>'
                             for i, s in enumerate(sections))
            st.markdown('<nav class="note-toc" aria-label="Table of contents">' + links + '</nav>', unsafe_allow_html=True)
        st.divider()
        st.download_button("Download note", content, file_name=source.path.name, mime="text/markdown",
                           on_click="ignore")
        if source.original_url:
            st.link_button("Open original document", source.original_url)
        st.caption("Your valuation edits stay in the original tab.")

    with st.container(key="note_article"):
        st.markdown('<div class="note-kicker"><span class="note-badge">' + escape(kind) + '</span>'
                    + escape(ticker) + '</div>', unsafe_allow_html=True)
        st.title(re.sub(r"(?<!\\)\$", r"\\$", title), anchor="note-title")
        byline = ("Agent-written analysis · Read-only" if kind == "Research note" else
                  "Valuation methodology · Read-only" if kind == "Methodology note" else
                  "Repository research and valuation rules · Read-only" if kind == "Research guidelines" else
                  "Source provenance and collection details · Read-only")
        st.markdown('<div class="note-byline">' + byline + '</div>', unsafe_allow_html=True)
        if result is not None:
            st.markdown('<span id="note-results"></span>', unsafe_allow_html=True)
            with st.expander("Search results" if search else "Referenced passages", expanded=True):
                st.caption(result.caption)
                for match in result.matches:
                    st.markdown("**" + match.label.replace("$", r"\$") + "**")
                    st.markdown(highlighted_excerpt(match), unsafe_allow_html=True)
        else:
            st.caption("Whole note · No specific passage was recorded in this link.")
        if intro:
            st.markdown(note_markdown(intro, index, source))
        for i, section in enumerate(sections):
            st.header(section.heading.replace("$", r"\$"), anchor=f"note-section-{i}")
            st.markdown(note_markdown(section.body, index, source))
        st.divider()
        with st.expander("Document details and raw text"):
            st.caption("Recorded citation: " + source.tag.replace("$", r"\$"))
            st.caption(source.file)
            if source.note:
                st.caption(source.note.replace("$", r"\$"))
            st.code(content, language=None, wrap_lines=True, height=450)
