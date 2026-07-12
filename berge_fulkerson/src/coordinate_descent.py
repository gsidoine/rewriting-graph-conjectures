"""Transparent coordinate-replacement operations for six matchings."""
from __future__ import annotations
from collections.abc import Sequence
from .state_encoding import quadratic_potential, replacement_weights


def replacement_delta(edges, matchings, index, replacement) -> int:
    weights = replacement_weights(edges, matchings, index)
    old = sum(weights[e] for e in matchings[index])
    new = sum(weights[e] for e in replacement)
    return new - old


def best_replacement(edges, matchings, index, candidates):
    weights = replacement_weights(edges, matchings, index)
    return min(candidates, key=lambda matching: sum(weights[e] for e in matching))


def strict_descent_step(edges, matchings, candidates):
    current_q = quadratic_potential(edges, matchings)
    best_state = tuple(matchings)
    best_q = current_q
    for index in range(6):
        replacement = best_replacement(edges, matchings, index, candidates)
        state = list(matchings)
        state[index] = replacement
        q = quadratic_potential(edges, state)
        if q < best_q:
            best_q, best_state = q, tuple(state)
    return best_state, best_q
