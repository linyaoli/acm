"""
https://www.hackerrank.com/challenges/filling-jars
"""
input = str(raw_input(''))
input = input.split(' ')
n = int(input[0])
m = int(input[1])
ans = 0
for i in xrange(m):
  input = str(raw_input(''))
  input = input.split(' ')
  ans = ans + (int(input[1]) - int(input[0]) + 1)* int(input[2])

print ans / n
