count = 0
n = 100
for i in xrange(1, n + 1):
    while i % 5 == 0:
        i = i / 5
        count += 1

print count
