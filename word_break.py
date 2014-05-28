#!/usr/bin/python
class Solution:
    def wordBreak(self, s, dict):
        _s = s
        while s != "":
            for i in range(1, len(s), 1):
                if s[0:i] in dict:
                    s = s[i:]
            if s == "":
                return True
            if s == _s:
                return False
            if s != _s:
                s = _s
        return True
