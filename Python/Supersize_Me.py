def super_size(n):
    assert(n >= 0)
    """Write the function that rearranges an integer into its largerst possible
    value.
    >>> super_size(123456)
    >>> 654321
    >>> super_size(105)
    >>> 510
    >>> super_size(12)
    >>> 21
    """
    if n < 10:
        return n
