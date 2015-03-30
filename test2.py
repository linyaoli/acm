n=5
#nodes = [4,4,4,4,4]
#visited = [-1] * n
nodes= [0,1,2,3,4]

def nchange(nodes):
    if nodes == []: return 0
    visited = [-1] * len(nodes)
    grp = 1
    npass = 0
    visited[0] = 0

    for i in xrange(len(nodes)):
        if dfs(nodes, visited, i, n):
            npass += 1
            grp += 1
    return grp - 1

def dfs(nodes, visited, i, curpass):
    if i == 0:
        return False

    if visited[i] > 0 and visited[i] != curpass:
        return False
    if visited[i] == curpass:
        return True
    visited[i] = curpass
    dfs(nodes, visited, nodes[i], curpass)


print nchange(nodes)
