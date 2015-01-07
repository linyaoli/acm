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

a = [[0 for i in xrange(10)] for i in xrange(10)]
#a = [0 for i in xrange(10)] * 10
a = a[::1]
print a

def b_search(a, x):
    n = len(a)
    start = 0
    end = n - 1
    while start <= end:
        mid = start + (end - start) / 2
        if x > a[mid]:
            start = mid + 1
        elif x < a[mid]:
            end = mid - 1
        else:
            return a[mid]

    return 0


def inorder(root):
    if root is None:
        return

    inorder(root.left)
    inorder(root)
    inorder(root.right)

def merge(A, m, B, n):
        len_a = m - 1
        len_b = n - 1
        i = m + n - 1
        while i >= 0 and len_b >= 0:
            if len_a < 0:
                A[i] = B[len_b]
                len_b -= 1
            elif A[len_a] > B[len_b]:
                A[i] = A[len_a]
                len_a -=1
            else:
                A[i] = B[len_b]
                len_b -=1
            i -= 1

        print A

a = [2,3, 0, 0]
b = [1,1]
merge(a, len(a)-len(b), b, len(b))
