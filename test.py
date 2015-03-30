n=5
nodes = [4,4,4,4,4]
visited = [-1] * n

def dfs(m, i, visited, nodes):
    if visited[i] == -1:
        visited[i] = m
        if nodes[i] != i:
            return dfs(m, nodes[i], visited, nodes)
        else:
            return i
    else:
        return visited[i]

for i in xrange(n):
    if visited[i] == -1:
        s = dfs(i, i, visited, nodes)
        if s != i:
            for j in xrange(n):
                if visited[j] == i:
                    visited[j] = s

count = [0] * n
sum = 0
for i in visited:
    if count[i] == 0:
        count[i] = 1
        sum += 1
if visited[0] == 0:
    sum -= 1

print sum
