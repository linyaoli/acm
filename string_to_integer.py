class Solution:
    # @return an integer
    def atoi(self, str):
        n = len(str)
        result = 0
        for digit in str:
            if digit == ' ':
                # discard whitespaces
                continue
