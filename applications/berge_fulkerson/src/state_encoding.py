"""State, multiplicity, and discrepancy routines."""
from __future__ import annotations
from collections import Counter
from collections.abc import Sequence

Edge = tuple[int, int]
Matching = frozenset[Edge]


def multiplicities(matchings: Sequence[Matching]) -> Counter[Edge]:
    result: Counter[Edge] = Counter()
    for matching in matchings:
        result.update(matching)
    return result


def quadratic_potential(edges: Sequence[Edge], matchings: Sequence[Matching]) -> int:
    mult = multiplicities(matchings)
    return sum((mult[edge] - 2) ** 2 for edge in edges)


def replacement_weights(edges: Sequence[Edge], matchings: Sequence[Matching], index: int) -> dict[Edge, int]:
    mult = multiplicities(matchings)
    current = matchings[index]
    return {edge: 2 * (mult[edge] - 2) + 1 - 2 * int(edge in current) for edge in edges}
