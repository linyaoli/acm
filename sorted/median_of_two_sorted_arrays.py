"""
Thoughts:

<> Surely we can merge, it takes O(n) time and O(n) space.

<> divide-and-conquer

To find kth node:

        +---------+---------+
Array A | part1   | part2   |
        +---------+---------+
        +---------------+---------------+
Array B | part3         | part4         |
        +---------------+---------------+


each time compare the k/2 th node in A and B arrays.
m = len(A) n = len(B)

If (m/2+n/2+1) > k && am/2 > bn/2 , drop Section 2
If (m/2+n/2+1) > k && am/2 < bn/2 , drop Section 4
If (m/2+n/2+1) < k && am/2 > bn/2 ,  drop Section 3
If (m/2+n/2+1) < k && am/2 < bn/2 ,  drop Section 1

=--------------------------------------------=

for a simpler median solution:

1) Calculate the medians m1 and m2 of the input arrays ar1[]
   and ar2[] respectively.
2) If m1 and m2 both are equal then we are done.
     return m1 (or m2)

3) If m1 is greater than m2, then median is present in one
   of the below two subarrays.
    a)  From first element of ar1 to m1 (ar1[0...|_n/2_|])
    b)  From m2 to last element of ar2  (ar2[|_n/2_|...n-1])

4) If m2 is greater than m1, then median is present in one
   of the below two subarrays.
   a)  From m1 to last element of ar1  (ar1[|_n/2_|...n-1])
   b)  From first element of ar2 to m2 (ar2[0...|_n/2_|])
   
5) Repeat the above process until size of both the subarrays
   becomes 2.
6) If size of the two arrays is 2 then use below formula to get
  the median.
    Median = (max(ar1[0], ar2[0]) + min(ar1[1], ar2[1]))/2


"""


class Solution:
    # @return a float
    def findMedianSortedArrays(self, A, B):
        na, nb = len(A), len(B)
        # the total num of A and B: 1. if odd: pick (m+n)/2 + 1; 2. if even, pick ((m+n)/2 + (m+n)/2+1)/2.
        if (na + nb) % 2 == 0:
            return (self.gen(A, B, (na + nb)/2) + self.gen(A, B, (na + nb)/2 + 1))/2.0
        else:
            return self.gen(A, B, (na + nb)/2 + 1)

    def gen(self, A, B, k):
        na, nb = len(A), len(B)
        # if length becomes 0, means the median is not in the array.
        if na == 0:
            return B[k - 1]
        if nb == 0:
            return A[k - 1]
        # k <= 1, means there are two elems left, either the first elem in A or B.
        if k <= 1:
            return min(A[0], B[0])

        if B[nb/2] >= A[na/2]:
            if (na / 2 + nb / 2 + 1) >= k:
                #drop the right part of B
                return self.gen(A, B[:nb/2], k)
            else:
                #drop the right part of A
                return self.gen(A[(na/2 + 1):], B, k - (na/2+1))
        else:
            if (na / 2 + nb / 2 + 1) >= k:
                #drop the left part of A
                return self.gen(A[:na/2], B, k)
            else:
                #drop the left part of B
                return self.gen(A, B[nb/2+1:], k - (nb/2 + 1))



sol = Solution()
A = [1,9,9,9,10,11,13]
B = [2,2,3,6,7,9,10]

print sol.findMedianSortedArrays(A,B)
