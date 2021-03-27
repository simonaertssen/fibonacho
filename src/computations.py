import functools


@functools.lru_cache(maxsize=None, typed=True)
def compute_fibonacci(n: int):
    if n < 2:
        return n
    return compute_fibonacci(n-1) + compute_fibonacci(n-2)
