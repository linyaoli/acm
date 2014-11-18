def gen(a, i, n, res):
    if i == n:
        print a
        res.append(a[:])
        print res
    else:
        for j in xrange(i, n) :
            a[i], a[j] = a[j], a[i]
            gen(a, i+1, n, res)
            a[i], a[j] = a[j], a[i]

a = [1, 2, 3]
gen(a, 0, 3, [])

print ord('A')

class a:
    def gen(self, b):
        b = 10
        print b

sol = a()
sol.gen(12)
