
def merge(A, m, B, n):
    len_a = m - 1
    len_b = n - 1
    i = m + n - 1
    A = A + [0] * n
    while i >= 0 and len_b >= 0:
        if len_a < 0:
            A[i] = B[len_b]
            len_b -= 1
        elif A[len_a] >= B[len_b]:
          A[i] = A[len_a]
          len_a -= 1
        else:
          A[i] = B[len_b]
          len_b -= 1
        print A
    i -= 1
    return

A = [2]
B = [1]
merge(A, 1, B, 1)
