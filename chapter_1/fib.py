from functools import lru_cache


from typing import Dict, Generator

memo: Dict[int, int] = {0: 0, 1: 1}


# Recursive approach
def fib1(n: int) -> int:
    if n < 2:
        return n
    return fib1(n - 1) + fib1(n - 2)


# Memoized implementation
def fib_memo(n: int) -> int:
    if n not in memo:
        memo[n] = fib_memo(n - 1) + fib_memo(n - 2)
    return memo[n]


# Automatic caching
@lru_cache(None)
def fib_auto_memo(n: int) -> int:
    if n < 2:
        return n
    return fib_auto_memo(n - 1) + fib_auto_memo(n - 2)


def fib_best(n: int) -> int:
    if n == 0:
        return n
    a: int = 0
    b: int = 1
    for _ in range(1, n):
        a, b = b, a + b
    return b


def fib_gen(n: int) -> Generator[int, None, None]:
    yield 0
    if n == 0:
        yield n
    a: int = 0
    b: int = 1
    for _ in range(1, n):
        a, b = b, a + b
    yield b


if __name__ == "__main__":
    print(fib1(n=5))
    print(fib1(n=10))
    print(fib_memo(n=5))
    print(fib_memo(n=10))
    print(fib_memo(n=100))
    print(fib_auto_memo(n=50))
    print(fib_best(n=50))
    for i in fib_gen(50):
        print(i)
