def farey(v, lim):
    """ No error checking on args.  lim = maximum denominator.
        Results are (numerator, denominator); (1, 0) is "infinity".
    """
    if v < 0:
        n, d = farey(-v, lim)
        return -n, d
    z = lim - lim    # Get a "0 of the right type" for denominator
    lower, upper = (z, z+1), (z+1, z)
    while True:
        mediant = (lower[0] + upper[0]), (lower[1] + upper[1])
        if v * mediant[1] > mediant[0]:
            if lim < mediant[1]:
                return upper
            lower = mediant
        elif v * mediant[1] == mediant[0]:
            if lim >= mediant[1]:
                return mediant
            if lower[1] < upper[1]:
                return lower
            return upper
        else:
            if lim < mediant[1]:
                return lower
            upper = mediant
