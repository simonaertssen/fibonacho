import functools


@functools.lru_cache(maxsize=None, typed=True)
def compute_fibonacci(n: int):
    """
    Compute the nth fibonacci number recursively. Cache the results
    for faster access, this greatly speeds up the time spent in this function.
    """
    if n < 2:
        return n
    return compute_fibonacci(n-1) + compute_fibonacci(n-2)


def fibonacci_single(n: int):
    return compute_fibonacci(n)


def fibonacci_list(keys: list):
    return [compute_fibonacci(k) for k in keys]
