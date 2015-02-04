class Solution:
    # @return a string
    def contains(self, dict1, dict2):
        for i in dict1:
            if dict1[i] < dict2[i]:
                return False
        return True

    def minWindow(self, S, T):
        # two pointers
        slow = 0
        fast = 0
        n = len(S)
        t_dict = {}
        for i in T:
            try:
                t_dict[i] += 1
            except:
                t_dict[i] = 1
        __t = t_dict.copy()
        for i in __t:
            __t[i] = 0

        res = S

        while fast < n:
            if self.contains(__t, t_dict):
                if S[fast] == S[slow]:
                    slow += 1
                    while slow < fast:
                        if S[slow] not in t_dict:
                            slow += 1
                        else:
                            __t[S[slow]] -= 1
                            if self.contains(__t, t_dict):
                                slow += 1
                            else:
                                __t[S[slow]] += 1
                                if fast - slow + 1 < len(res):
                                    res = S[slow:fast+1]
                                break
                else:
                    if S[fast] in __t:
                        __t[S[fast]] += 1

            elif S[fast] in __t:
                __t[S[fast]] += 1
                if __t == t_dict:
                    if fast - slow + 1 < len(res):
                        res = S[slow:fast+1]
                    continue
            fast += 1
        return res



sol = Solution()
print sol.minWindow("ADOBECOEBANC", "ABC")
