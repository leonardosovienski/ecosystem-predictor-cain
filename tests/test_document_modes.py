"""Canonical state documents declare their mode (closure audit 2026-10-08; mirrors cain/tests/test_canonical_state.py).

A living document declares exactly one ``MODE: CURRENT_LIVING_STATE``; a snapshot declares ``MODE: SNAPSHOT_IMMUTABLE``
with AS_OF_DATE, AS_OF_SHA and SUPERSEDED_BY. No other rule: this is a declaration check, not a content check.
"""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LIVING = ["CURRENT_STATE.md", "HANDOFF.md", "ETAPA_B_INTEGRATED_STACK_20260928.md"]
SNAPSHOTS = ["ECOSYSTEM_CURRENT_STATE.md", "docs/archive/CURRENT_STATE_camadas_2026-09-30_a_2026-10-07.md"]


def _declarations(text: str) -> list[str]:
    return re.findall(r"^>? ?MODE: (SNAPSHOT_IMMUTABLE|CURRENT_LIVING_STATE)", text, flags=re.M)


def test_living_documents_declare_the_living_mode_only() -> None:
    for relative in LIVING:
        assert _declarations((ROOT / relative).read_text(encoding="utf-8")) == ["CURRENT_LIVING_STATE"], relative


def test_snapshot_documents_declare_date_sha_and_successor() -> None:
    for relative in SNAPSHOTS:
        text = (ROOT / relative).read_text(encoding="utf-8")
        assert _declarations(text) == ["SNAPSHOT_IMMUTABLE"], relative
        assert re.search(r"AS_OF_DATE: \d{4}-\d{2}-\d{2}", text), relative
        assert re.search(r"SUPERSEDED_BY: \S+", text), relative
