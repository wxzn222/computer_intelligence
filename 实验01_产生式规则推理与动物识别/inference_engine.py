"""可追踪的前向推理引擎。"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

from knowledge_base import ANIMALS, Rule


@dataclass(frozen=True)
class FiredRule:
    round_no: int
    rule_id: str
    premises: tuple[str, ...]
    conclusion: str


@dataclass(frozen=True)
class InferenceResult:
    initial_facts: frozenset[str]
    all_facts: frozenset[str]
    fired_rules: tuple[FiredRule, ...]
    animals: tuple[str, ...]


def forward_chain(
    initial_facts: Iterable[str], rules: Iterable[Rule]
) -> InferenceResult:
    """反复匹配规则，直到一轮中没有产生新事实。"""

    initial = frozenset(initial_facts)
    known = set(initial)
    trace: list[FiredRule] = []
    fired_ids: set[str] = set()
    round_no = 0

    while True:
        round_no += 1
        changed = False
        for rule in rules:
            can_fire = (
                rule.rule_id not in fired_ids
                and rule.premises.issubset(known)
            )
            if not can_fire:
                continue

            fired_ids.add(rule.rule_id)
            if rule.conclusion in known:
                continue

            known.add(rule.conclusion)
            changed = True
            trace.append(
                FiredRule(
                    round_no,
                    rule.rule_id,
                    tuple(sorted(rule.premises)),
                    rule.conclusion,
                )
            )

        if not changed:
            break

    animals = tuple(sorted(known.intersection(ANIMALS)))
    return InferenceResult(initial, frozenset(known), tuple(trace), animals)
