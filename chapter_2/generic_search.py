from __future__ import annotations
from typing import (
    TypeVar,
    Iterable,
    Sequence,
    Generic,
    List,
    Callable,
    Set,
    Deque,
    Dict,
    Any,
    Optional,
)
from typing_extensions import Protocol
from heapq import heappush, heappop


T = TypeVar("T")
C = TypeVar("C", bound="Comparable")


def linear_contains(iterable: Iterable[T], key=T) -> bool:
    for item in iterable:
        if item == key:
            return True
    return False


class Comparable(Protocol):
    def __eq__(self, other: Any) -> bool:
        ...

    def __lt__(self: C, other: C) -> bool:
        ...

    def __gt__(self: C, other: C) -> bool:
        return (not self < other) and self != other

    def __le__(self: C, other: C) -> bool:
        return self < other or self == other

    def __ge__(self: C, other: C) -> bool:
        return not self < other


def binary_contains(sequence: Sequence[C], key: C) -> bool:
    low: int = 0
    high: int = len(sequence) - 1
    while low <= high:
        middle: int = (low + high) // 2
        if sequence[middle] < key:
            low = middle + 1
        elif sequence[middle] > key:
            high = middle - 1
        else:
            return True
    return False


if __name__ == "__main__":
    assert linear_contains([1, 5, 15, 15, 15, 15, 20], 5)  # True
    assert binary_contains(["a", "d", "e", "f", "z"], "f")  # type: ignore
    assert not binary_contains(["john", "mark", "ronald", "sarah"], "sheila")  # type: ignore
