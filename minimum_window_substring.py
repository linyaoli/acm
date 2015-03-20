"""
Given a string S and a string T, find the minimum window in S which will contain
all the characters in T in complexity O(n).

For example,
S = "ADOBECODEBANC"
T = "ABC"
Minimum window is "BANC".

"""
# Use two pointers : start and end of the window
# First move the end pointer in S
# if one window has all the chars in T
# move the start pointer until minimize the window.

class Solution:
    # @return a string
    def minWindow(self, S, T):
        # @var count1 : appear count
        # @var count2 : expect count
        count1={}; count2={}
        for char in T:
            if char not in count1: count1[char]=1
            else: count1[char]+=1

            if char not in count2: count2[char]=1
            else: count2[char]+=1

        count=len(T)
        start=0; minSize=100000; minStart=0

        for end in range(len(S)):
            if S[end] in count2 and count2[S[end]]>0:
                count1[S[end]]-=1
                if count1[S[end]]>=0:
                    count-=1

            if count == 0:
                # currently the window has all chars in T.
                while True:
                    if S[start] in count2 and count2[S[start]]>0:
                        if count1[S[start]]<0:
                            count1[S[start]]+=1
                        else:
                            break
                    start+=1
                if minSize>end-start+1:
                    minSize=end-start+1; minStart=start
        if minSize==100000: return ''
        else:
            return S[minStart:minStart+minSize]



sol = Solution()
print sol.minWindow("ADOBECOEBANC", "ABC")
