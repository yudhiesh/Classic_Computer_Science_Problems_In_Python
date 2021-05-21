from typing import TypeVar, Generic, List

T = TypeVar("T")


class Stack(Generic[T]):
    def __init__(self) -> None:
        self._container: List[T] = []

    def push(self, item: T) -> None:
        self._container.append(item)

    def pop(self) -> T:
        return self._container.pop()

    def __repr__(self) -> str:
        return repr(self._container)


def hanoi(begin: Stack[int], end: Stack[int], temp: Stack[int], n: int) -> None:
    if n == 1:
        end.push(begin.pop())
    else:
        # Move the upper n-1 discs from tower A to B using C as the in-between
        hanoi(begin, temp, end, n - 1)
        # Move the single lowest disc from A to C
        hanoi(begin, end, temp, 1)
        # Move the n-1 discs from tower B to C using A
        hanoi(temp, end, begin, n - 1)


if __name__ == "__main__":
    num_disc: int = 10
    tower_a: Stack[int] = Stack()
    tower_b: Stack[int] = Stack()
    tower_c: Stack[int] = Stack()

    for i in range(1, num_disc + 1):
        tower_a.push(i)

    hanoi(tower_a, tower_c, tower_b, num_disc)
    print(tower_a)
    print(tower_b)
    print(tower_c)
