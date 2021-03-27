def to_positive_integer(n):
    """
    Make the input an integer and raise an error is there is a negative number
    """
    n = int(n)
    if n < 0:
        raise ValueError
    return n


def validate_input(validate_me):
    """
    Check input for non-allowed tokens and make a positive integer if possible
    """
    try:
        if isinstance(validate_me, str):
            raise TypeError
        validate_me = to_positive_integer(validate_me)
    except (TypeError, ValueError):
        raise
    return validate_me
