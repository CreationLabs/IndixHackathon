def editDistance(s1, s2):
    """Computes the Levenshtein distance between two arrays (strings too).
    Such distance is the minimum number of operations needed to transform one array into
    the other, where an operation is an insertion, deletion, or substitution of a single
    item (like a char). This implementation (Wagner-Fischer algorithm with just 2 lines)
    uses O(min(|s1|, |s2|)) space.

    editDistance([], [])
    0
    >>> editDistance([1, 2, 3], [2, 3, 5])
    2
    >>> tests = [["", ""], ["a", ""], ["", "a"], ["a", "a"], ["x", "a"],
    ...          ["aa", ""], ["", "aa"], ["aa", "aa"], ["ax", "aa"], ["a", "aa"], ["aa", "a"],
    ...          ["abcdef", ""], ["", "abcdef"], ["abcdef", "abcdef"],
    ...          ["vintner", "writers"], ["vintners", "writers"]];
    >>> [editDistance(s1, s2) for s1,s2 in tests]
    [0, 1, 1, 0, 1, 2, 2, 0, 1, 1, 1, 6, 6, 0, 5, 4]
    """
    # This function is designed for Psyco
    if s1 == s2: return 0 # this is fast in Python
    if len(s1) > len(s2):
        s1, s2 = s2, s1
    r1 = range(len(s2) + 1)
    r2 = [0] * len(r1)
    i = 0
    for c1 in s1:
        r2[0] = i + 1
        j = 0
        for c2 in s2:
            if c1 == c2:
                r2[j+1] = r1[j]
            else:
                a1 = r2[j]
                a2 = r1[j]
                a3 = r1[j+1]
                if a1 > a2:
                    if a2 > a3:
                        r2[j+1] = 1 + a3
                    else:
                        r2[j+1] = 1 + a2
                else:
                    if a1 > a3:
                        r2[j+1] = 1 + a3
                    else:
                        r2[j+1] = 1 + a1
            j += 1
        aux = r1; r1 = r2; r2 = aux
        i += 1
    return r1[-1]


def editDistanceFast(s1, s2, r1=[0]*35, r2=[0]*35):
    """Computes the Levenshtein distance between two arrays (strings too).
    Such distance is the minimum number of operations needed to transform one array into
    the other, where an operation is an insertion, deletion, or substitution of a single
    item (like a char). This implementation (Wagner-Fischer algorithm with just 2 lines)
    uses O(min(|s1|, |s2|)) space.

    This version is a bit faster but it works only with strings up to 34 items long.

    editDistanceFast([], [])
    0
    >>> editDistanceFast([1, 2, 3], [2, 3, 5])
    2
    >>> tests = [["", ""], ["a", ""], ["", "a"], ["a", "a"], ["x", "a"],
    ...          ["aa", ""], ["", "aa"], ["aa", "aa"], ["ax", "aa"], ["a", "aa"], ["aa", "a"],
    ...          ["abcdef", ""], ["", "abcdef"], ["abcdef", "abcdef"],
    ...          ["vintner", "writers"], ["vintners", "writers"]];
    >>> [editDistanceFast(s1, s2) for s1,s2 in tests]
    [0, 1, 1, 0, 1, 2, 2, 0, 1, 1, 1, 6, 6, 0, 5, 4]
    """
    # This function is designed for Psyco
    if s1 == s2: return 0 # this is fast in Python
    if len(s1) > len(s2):
        s1, s2 = s2, s1
    len_s2 = len(s2)
    assert len(s2) <= 34, "Error: one input sequence is too much long (> 34), use editDistance()."
    for i in xrange(len_s2 + 1):
        r1[i] = i
        r2[i] = 0
    i = 0
    for c1 in s1:
        r2[0] = i + 1
        j = 0
        for c2 in s2:
            if c1 == c2:
                r2[j+1] = r1[j]
            else:
                a1 = r2[j]
                a2 = r1[j]
                a3 = r1[j+1]
                if a1 > a2:
                    if a2 > a3:
                        r2[j+1] = 1 + a3
                    else:
                        r2[j+1] = 1 + a2
                else:
                    if a1 > a3:
                        r2[j+1] = 1 + a3
                    else:
                        r2[j+1] = 1 + a1
            j += 1
        aux = r1; r1 = r2; r2 = aux
        i += 1
    return r1[len_s2]


