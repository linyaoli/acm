import heapq
import random

class TopkHeap(object):
    def __init__(self, k):
        self.k = k
        self.data = []

    def Push(self, elem):
        if len(self.data) < self.k:
            heapq.heappush(self.data, elem)
        else:
            topk_small = self.data[0]
            if elem > topk_small:
                heapq.heapreplace(self.data, elem)

    def TopK(self):
        return [x for x in reversed([heapq.heappop(self.data) for x in xrange(len(self.data))])]

if __name__ == "__main__":
    print "Hello"
    list_rand = random.sample(xrange(1000000), 100)
    th = TopkHeap(3)
    for i in list_rand:
        th.Push(i)
    print th.TopK()
    print sorted(list_rand, reverse=True)[0:3]

#ASC & DESC

import heapq
h = []
heapq.heappush(h, (5, 'write code'))
heapq.heappush(h, (7, 'release product'))
heapq.heappush(h, (1, 'write spec'))
heapq.heappush(h, (3, 'create tests'))
print heapq.heappop(h)

a = "1234"
print a[:3]
idx = ["shash","shank","shashank","sha"]
di = {}
for i in range(0, 10, 1):
    for j in range(0, len(idx), 1):
        if i >= len(idx[j]):
            continue
        tmp = idx[j]
#        print tmp[0:i+1]
        if tmp[0:i+1] not in di:
            di[tmp[0:i+1]] = 1
        else:
            di[tmp[0:i+1]] += 1
print di


src = "abcd"
src = list(src)
def permu ( src, count ):
    for idx in range(count, len(src), 1):
        src[idx] = src[idx].upper()
        print src
        count += 1
        permu(src, count)
        src[idx] = src[idx].lower()



permu(src, 0)




idx = [(1,2), (2,3), (3,5), (6,8.5), (8,9), (8.5, 10), (11, 12), (12,13)]

idx_len = 0
idx_max = 0

for i in range(0, len(idx) - 1, 1):
    if idx[i][1] >= idx[i+1][0]:
        idx_len = 0
    else:
        idx_len += 1
        if idx_len > idx_max:
            idx_max = idx_len
idx_max += 1

print idx_max



idx = ['cat', 'dog', 'tac', 'god', 'cta', 'dgo', 'tca', 'asd', 'dsa', 'cat', 'car', 'dgo']
print idx

def check_anagram( src, dst ):
    idx = {}
    for c1 in src:
        if c1 not in idx:
            idx[c1] = 1
        else:
            idx[c1] += 1
    for c2 in dst:
        if c2 not in idx:
            return -1
        else:
            idx[c2] -= 1

    for c1 in idx:
        if idx[c1] != 0:
            return -1
    return 1

def swap( src, dst ):
    tmp = src
    src = dst
    dst = tmp
    return src, dst

def sort_anagram( src ):
    for i in range(0, len(src)-1, 1):
        count = 0
        for j in range(i+1, len(src), 1):
            if check_anagram(src[i], src[j]) == 1:
                src[i+1], src[j] = swap(src[i+1], src[j])
                count += 1
        i += count

    print src

sort_anagram(idx)



#
# Your previous C++ content is preserved below:
#
# #include <iostream>
# using namespace std;
#
# // To execute C++, please define "int main()"
#
# int main() {
#   int *a = new int[10];
#   a[0] = 1;
#   for (int i = 0; i < 5; i++) {
#     cout << "hello world\n";
#     cout<<a[0];
#   }
#   free(a);
#   return 0;
# }
#
#
# /*
# Your previous Python content is preserved below:
#
# a = "abcd1abdc1d"
# tmp = ""
#
# for c in range(0, len(a), 1):
#     t = a[c]
#     if t == '1':
#         t = "%20"
#     tmp += t
#
# print tmp
#
# ###########
#
# s = "abbccccddeef"
# s += "#"
# count = 0
# a = s[0]
# _s = ""
#
# for ch in s:
#     if a == ch:
#         count = count + 1
#     if a != ch:
#         _s += a
#         _s += str(count)
#         a = ch
#         count = 1
#
#
# print _s
#
# class node:
#     def __init__(self, val):
#         self.val = val
#         self.next = None
#
# n = node(3)
# nn = node(10)
# n.next = nn
# print n.next.val, nn.val
#
# ########################
#
# a = []
# a.append("123")
# print a
#
# a = {}
# a["li"] = "linyao"
# print a
# a["li"] = "123"
# a["z"] = "zhang"
# print a
#
#
#
#
#  */
