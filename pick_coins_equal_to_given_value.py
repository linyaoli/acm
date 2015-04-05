def coins(cns, i, ret, n):
    if sum(ret) == n:
        print ret
    elif sum(ret) > n:
        return
    else:
        for j in xrange(i, len(cns)):
            ret.append(cns[j])
            coins(cns, j, ret, n)
            ret.pop()


coins([1, 5, 10, 25], 0, [], 16)
