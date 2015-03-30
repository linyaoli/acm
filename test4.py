nodes=[(0,0),(1,1),(2,2),(3,3),(4,4)]
n = len(nodes)
parent=[0]*n
for i in xrange(n):
    parent[i] = -1

for i in nodes:
    parent[i[1]] = i[0]

def find(x):
    global parent
    if parent[x] == x:
        return x
    else:
        return find(parent[x])

def union(x, y):
    global parent
    xroot = find(x)
    yroot = find(y)
    parent[xroot] = yroot


for i in xrange(n):
    for j in xrange(n):
        if nodes[j] == i:
            if find(i) != find(j):
                union(i, j)

r = 0
for i in xrange(len(nodes)):
    if parent[i] == -1:
        r += 1

print r-1
