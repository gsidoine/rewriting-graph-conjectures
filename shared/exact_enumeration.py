"""Generic reverse-reachability for finite normalization systems."""
from __future__ import annotations
from collections import deque
from collections.abc import Callable, Iterable
from typing import Hashable, TypeVar

S = TypeVar("S", bound=Hashable)


def reverse_reachable(
    states: Iterable[S],
    targets: Iterable[S],
    successors: Callable[[S], Iterable[S]],
) -> set[S]:
    """Return states reaching a target when every forward edge is supplied.

    This intentionally favors transparent independent checking over speed.
    """
    states = tuple(states)
    reverse: dict[S, list[S]] = {state: [] for state in states}
    for state in states:
        for nxt in successors(state):
            reverse.setdefault(nxt, []).append(state)
    reached = set(targets)
    queue = deque(reached)
    while queue:
        current = queue.popleft()
        for predecessor in reverse.get(current, ()):
            if predecessor not in reached:
                reached.add(predecessor)
                queue.append(predecessor)
    return reached
