"""
https://www.hackerrank.com/contests/noi-ph/challenges/color-grid
"""

input = raw_input().split()
N = int(input[0])
P = int(input[1])

result = 0
check = {}
check['COL'] = {}
check['ROW'] = {}
records = []

for i in xrange(P):
  records += [raw_input().split()]


for i in range(P-1, -1, -1):
  if records[i][0] == 'COL':
    if records[i][1] not in check['COL']:
      result += int(records[i][2]) * (N - len(check['ROW']))
      check['COL'][records[i][1]] = 1
  else:
    if records[i][1] not in check['ROW']:
      result += int(records[i][2])* (N - len(check['COL']))
      check['ROW'][records[i][1]] = 1


print result

