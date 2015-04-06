# find connected area by '1'.
# 110110
# 001000
# 110100
# return 5
input = [[1,1,0,1,1,0], [0,0,1,0,0,0], [1,1,0,1,0,0]]
count = 0
aha = 0
def helper(input, i, j, visited):
    global aha
    if i < 0 or j < 0 or i >= len(input) or j >= len(input[0]) or input[i][j] == 0:
        return
    aha += 1
    if input[i][j] == 1 and not visited[i][j]:
            visited[i][j] = True
            helper(input, i - 1, j, visited)
            helper(input, i, j - 1, visited)
            helper(input, i + 1, j, visited)
            helper(input, i, j + 1, visited)

visited = [[False for _ in xrange(len(input[0]))] for _ in xrange(len(input))]
for i in xrange(len(input)):
    for j in xrange(len(input[i])):
        if not visited[i][j] and input[i][j] == 1:
            helper(input, i, j, visited)
            count += 1
print count
print aha
