def isMultiple(ss):
    n = len(ss)

    for i in xrange(2, n/2 + 1):
        # so the substring is at least len = 2, and the string must at least combined by 2 substrings.
        it = 0
        print ss[:i], ss[i:2*i], 2*i + it
        while ss[:i] == ss[i + it:2*i + it] and 2*i + it <= n:
            if 2*i + it == n:
                return True
            it += i

    return False

print isMultiple("ABABCABABC")
