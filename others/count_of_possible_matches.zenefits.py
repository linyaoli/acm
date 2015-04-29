s1 = "waeginsapnaabangpisebbasepgnccccapisdneefngaabndlrjngeuiogbbegbuoeccccee"
#s1 = "waeginsapnaabangpisebbasepgnccccapisdnfngaabndlrjngeuiogbbegbbuoeccccee"
#s2 = "a+b+c-"
s1 = "aabbabbcccc"
s2 = ['aa', 'bb', 'cccc']
# O(n^3) time O(n^2) space

idx = [[] for _ in xrange(len(s2))]


for i in xrange(len(s2)):
    for j in xrange(len(s1) - len(s2[i]) + 1):
        if s1[j:j+len(s2[i])] == s2[i]:
            idx[i].append(j)

####
ret = [1] * len(s2)
for i in xrange(1, len(idx)):
    tmp = [0] * len(s2)
    for j in xrange(len(idx[i])):
        for k in xrange(len(idx[i-1])):
            if idx[i-1][k] < idx[i][j]:
                tmp[j] += ret[k]
    ret = tmp

print sum(ret)
