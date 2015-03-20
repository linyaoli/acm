"""
   ----       ---
  / 300 = 10 / 3

"""
import math

num = 32000
exact = int(math.sqrt(300))
factors = {}
for i in xrange(exact, 1, -1):
    term = i ** 2
    if num % term != 0:
        continue
    else:
        num /= term
    try:
        factors[i] += 1
    except:
        factors[i] = 1

print factors, num
