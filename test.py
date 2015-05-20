def solution1(S):
    # write your code in Python 2.7
    stack = []
    MAX = 2**12 -1 # 0~4095
    for i in S:
        if i.isdigit():
            stack.append(int(i))
        else:
            if len(stack) < 2: return -1
            a = stack.pop()
            b = stack.pop()
            if i == '+':
                if MAX - a < b: return -1
                stack.append(a + b)
            elif i == '*':
                if MAX * 1.0 / a < b: return -1
                stack.append(a * b)
            else:
                return - 1

    if len(stack) != 1: return -1
    return stack[0]

# you can use print for debugging purposes, e.g.
# print "this is a debug message"
print solution1("12*2+")

def solution(K, A):
    # write your code in Python 2.7
    #A = sorted(A)
    l = 0
    r = len(A) - 1
    table = {}
    cnt = 0
    for i in xrange(len(A)):
        if A[i] in table:
            table[A[i]].append(i)
        else:
            table[A[i]] = [i]

    for i in xrange(len(A)):
        if K - A[i] in table:
            cnt += len(table[K - A[i]])
    return cnt

#print solution(6, [1,8,-3,0,1,3,-2,4,5])
#print solution(8, [-4, 12, 4,4,2**31,4])
print solution(2, [-2, -10, 12, 4 ,1,1])
print solution(2, [1,1,1,1,1])
