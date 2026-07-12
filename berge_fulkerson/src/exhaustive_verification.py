"""Finite state-space verification for small cubic graphs."""
from __future__ import annotations
from collections import deque
from itertools import combinations_with_replacement
from .state_encoding import quadratic_potential


def verify_all_states_normalize(edges, perfect_matchings, tuple_size: int = 6):
    states = list(combinations_with_replacement(range(len(perfect_matchings)), tuple_size))
    qval = {
        state: quadratic_potential(edges, [perfect_matchings[i] for i in state])
        for state in states
    }
    targets = [state for state in states if qval[state] == 0]
    reverse = {state: [] for state in states}
    for state in states:
        for position in range(tuple_size):
            base = list(state[:position] + state[position + 1 :])
            for replacement in range(len(perfect_matchings)):
                nxt = tuple(sorted(base + [replacement]))
                if qval[nxt] <= qval[state]:
                    reverse[nxt].append(state)
    reached = set(targets)
    queue = deque(targets)
    while queue:
        current = queue.popleft()
        for pred in reverse[current]:
            if pred not in reached:
                reached.add(pred)
                queue.append(pred)
    return {
        "perfect_matchings": len(perfect_matchings),
        "states": len(states),
        "targets": len(targets),
        "reached": len(reached),
        "unresolved": len(states) - len(reached),
    }
