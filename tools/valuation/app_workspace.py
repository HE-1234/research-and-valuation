"""Editing aids and live comparison, with all valuation results supplied by the engine."""
from copy import deepcopy

import streamlit as st

from valuation.app_core import (
    CASE_LABELS, _WIDE, _save_cb, baseline_values, bump_gen,
    describe_path, file_changed_on_disk, md, per_share, review_only, set_in, show_value,
    unsaved_changes, working,
)
from valuation.schema import get_path, validate


def restore_cell(path: str) -> None:
    """Restore only this factor in this case; other experiments remain untouched."""
    original = get_path(st.session_state['loaded_doc'], path)
    set_in(working(), path, deepcopy(original))
    bump_gen()


def saved_comparison(path: str) -> None:
    original = get_path(st.session_state.get('loaded_doc', {}), path)
    now = get_path(working(), path)
    if original != now:
        _, kind = describe_path(path)
        st.caption('Saved assumption: ' + show_value(original, kind) + ' · Your edit is unsaved.')


def factor_reset(path: str) -> None:
    changed = get_path(st.session_state.get('loaded_doc', {}), path) != get_path(working(), path)
    st.button('Reset this assumption', key='reset:' + path, disabled=not changed,
              on_click=restore_cell, args=(path,), help='Restore this assumption to the version loaded from the file.')


def unavailable_value_summary(ctx, name: str) -> str:
    """Keep the sticky strip compact; the Model checks page retains complete failure messages."""
    if review_only():
        return 'Valuation results are deferred during draft review.'
    if name == 'weighted':
        return 'Needs all three cases and valid weights. See Model checks.'
    checks = validate({k: v for k, v in ctx.doc.items() if k != '_path'})
    if name in checks.skipped:
        return 'This case is guidance only. See Scenarios for its coverage.'
    issues = set(checks.shared_nulls + checks.stopped.get(name, []))
    if issues:
        count = len(issues)
        return f'{count} input{"s" if count != 1 else ""} need{"s" if count == 1 else ""} attention. See Model checks.'
    if ctx.market is None:
        return 'Market inputs are incomplete. See Overview.'
    return f'{CASE_LABELS[name]} case needs attention. See Model checks.'


def case_value(ctx, name: str) -> None:
    result = ctx.result
    if result and name in result.scenarios:
        value = result.scenarios[name].per_share
        loaded = baseline_values(result).get(name)
        change = '' if loaded is None else f' · {value - loaded:+,.2f} since load'
        st.caption(f'Current {CASE_LABELS[name].lower()} value: USD {per_share(value)} per share{change}')
    else:
        st.caption(f'Current {CASE_LABELS[name].lower()} value unavailable. ' + unavailable_value_summary(ctx, name))
    story = get_path(ctx.doc, f'scenarios.{name}.story')
    if story:
        with st.expander('Cross-reference: this case’s story'):
            st.markdown(md(story))


def live_panel(ctx) -> None:
    """Compact sticky value strip; navigation keeps its own uncluttered sidebar."""
    with st.container(key='live_value'):
        pick, current, price, actions = st.columns([1.25, 1.15, 1, 1.3], gap="medium")
        choices = ['base', 'bear', 'bull', 'weighted']
        if 'management' in (ctx.doc.get('scenarios') or {}):
            choices.append('management')
        if st.session_state.get('watch_case') not in choices:
            st.session_state['watch_case'] = 'base'
        with pick:
            name = st.selectbox('Case to watch', choices, key='watch_case',
                               format_func=lambda n: {'weighted': 'Weighted average', 'base': 'Base case',
                                   'bear': 'Bear case', 'bull': 'Bull case', 'management': 'Management'}.get(n, n))
        result = ctx.result
        selected = None if result is None else (result.weighted if name == 'weighted' else result.scenarios.get(name))
        with current:
            if selected is None:
                st.markdown('**Value unavailable**')
                st.caption(unavailable_value_summary(ctx, name))
            else:
                value = selected.per_share
                loaded = baseline_values(result).get(name)
                st.metric('Current value', per_share(value),
                          delta=None if loaded is None else f'{value - loaded:+,.2f} since load', delta_color='off')
                if loaded is not None:
                    st.caption(f'At load: USD {per_share(loaded)}')
        with price:
            st.metric('Market price', per_share(ctx.market.price) if ctx.market else 'Unavailable')
            if ctx.market:
                st.caption(f'Market price: USD {per_share(ctx.market.price)}')
            st.caption('USD per share')
        with actions:
            stale = file_changed_on_disk(ctx.path)
            diff = [] if stale else unsaved_changes(ctx.doc, ctx.path)
            with st.popover('Review & save' + (f' · {len(diff)}' if diff else ''), **_WIDE):
                st.markdown('**Your assumption changes**')
                if stale:
                    st.warning('The file changed on disk. Go to Review & save and start over to reload it before saving.')
                elif diff:
                    # Vertical entries fit the quick-review popover even when the change is a long story.
                    for change in diff:
                        label, kind = describe_path(change.path)
                        st.markdown('**' + md(label) + '**')
                        st.caption('Saved: ' + md(change.file_value if kind == 'text' else show_value(change.file_value, kind)))
                        st.markdown('Now: ' + md(change.current_value if kind == 'text' else show_value(change.current_value, kind)))
                else:
                    st.caption('All assumptions match the saved file.')
                note_key = f'quick_save_note:{ctx.ticker}'
                st.text_input('Why did you change these assumptions? (optional)', key=note_key)
                st.button('Save assumptions', key='quick_save', type='primary', disabled=stale or not diff,
                          on_click=_save_cb, args=(ctx.root, ctx.ticker, ctx.path, note_key), **_WIDE)
