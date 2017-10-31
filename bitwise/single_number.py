#!/usr/bin/python
class Solution:
    def singleNumber(self, A):
        res = 0
        for elem in A:
            res = res ^ elem

        return res

