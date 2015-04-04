"""
Given a number, find the next smallest palindrome larger than this number.
For example, if the input number is "2 3 5 4 5", the output should be "2 3 6 3 2".
And if the input number is "9 9 9", the output should be "1 0 0 1".
"""
class Solution:
    def nextPalindrome(self, num):
        # brute force O(n^2)
        # 9 9 9 -> 1 0 0 1
        # 1 2 1 4 -> 1 2 2 1
        # 1 2 3 5 -> 1 4 4 1
        # 1 2 2 1 -> 1 3 3 1
        n = len(num)
        mid = n / 2
        leftSmaller = False
        i = mid - 1
        j = mid + n % 2
        #pass those same digits
        while i >= 0 and num[i] == num[j]:
            i += 1
            j -= 1

        #if the left side number is smaller than
        # reversed right side number,
        #it means that the next palindrome number
        #must have larger left side.
        if i < 0 or num[i] < num[j]:
            leftSmaller = True
        #copy the left side to right
        while i >= 0:
            num[j] = num[i]
            j += 1
            i -= 1
        # 7 3 5 8 7 -> 7 3 5 3 7
        #if left is larger, that means the number is already
        #the next smallest palindrome number.
        #else,
        if leftSmaller == True:
            carry = 1
            i = mid - 1
            if n % 2 == 1:
                #add 1 to the mid number if the length is odd.
                num[mid] += carry
                #7 3 5 3 7 -> 7 3 6 3 7
                # if is 7 3 9 3 7 -> 7 3 10 3 7
                # carry up
                carry = num[mid] / 10
                num[mid] %= 10
                j = mid + 1
            else:
                #does nothing is even length
                j = mid
            # copy the left to right again,
            # care with the value of carry.
            while i >= 0:
                num[i] += carry
                carry = num[i] / 10
                num[i] %= 10
                num[j] = num[i]
                j += 1
                i -= 1

        return num

    def helper(self, num):
        # this function is used to handle all '9' number.
        pass

sol = Solution()
print sol.nextPalindrome([7,3,9,8,2])#2 3 6 3 2
