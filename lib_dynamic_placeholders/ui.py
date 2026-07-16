"""Shared Gradio helpers for consistent headings, descriptions, and help text."""

from __future__ import annotations

from contextlib import contextmanager
from typing import Iterator

import gradio as gr


def section_description(html: str) -> gr.HTML:
    """Intro copy under a section/accordion heading (same type as field help)."""
    return gr.HTML(f'<p class="dynph-ui-desc dynph-ui-intro">{html}</p>')


def field_help(html: str) -> gr.HTML:
    """Description placed immediately under a control (same look as section copy)."""
    return gr.HTML(f'<p class="dynph-ui-desc">{html}</p>')


@contextmanager
def setting_block() -> Iterator[None]:
    """
    One setting: control(s) then ``field_help``.

    Shared spacing so checkboxes, textboxes, and other inputs stack evenly.
    """
    with gr.Group(elem_classes=["dynph-setting"]):
        yield
