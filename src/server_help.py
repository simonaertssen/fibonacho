def to_positive_integer(n):
    n = int(n)
    if n < 0:
        raise ValueError
    return n


def validate_input(validate_me):
    try:
        if isinstance(validate_me, str):
            raise TypeError
        validate_me = to_positive_integer(validate_me)
    except (TypeError, ValueError):
        raise
    return validate_me
