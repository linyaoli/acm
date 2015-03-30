import collections as cc
def indices_dict(lis):
    d = cc.defaultdict(list)
    for i in lis:
        d[i[1]].append(i[0])
    return d

def disjoint_indices(lis):
    d = indices_dict(lis)
    sets = []
    while len(d):
        que = set(d.popitem()[1])
        ind = set()
        while len(que):
            ind |= que
            tmp = set()
            for i in que:
                for x in lis[i]:
                    for y in d.pop(x, []):
                        tmp.add(y)

            que = tmp - ind

        sets += [ind]
    #print sets
    return len(sets) - 1

def disjoint_sets(lis):
    return [set([x for i in s for x in lis[i]]) for s in disjoint_indices(lis)]

lis = [(0, 1), (1,0),(2,3),(3,4),(4,3)]
lis[0] = (0, 0)

print disjoint_indices(lis)
