def group_by(s, fn):
    """
    >>> group_by([12, 23, 14, 45], lambda p: p // 10)
    {1: [12, 14], 2: [23], 4: [45]}
    >>> group_by(range(-3, 4), lambda x: x * x)
    {9: [-3, 3], 4: [-2, 2], 1: [-1, 1], 0: [0]}
    """
    grouped = {}
    for x in range(len(s)):
        key = fn(s[x])
        if key in grouped:
            grouped[key].append(s[x])
        else:
            grouped[key] = (s[x])
    return grouped
