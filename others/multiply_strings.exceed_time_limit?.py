class Solution:
    # @param num1, a string
    # @param num2, a string
    # @return a string
    def multiply(self, num1, num2):
        n1 = len(num1)
        n2 = len(num2)
        if n1 > n2:
            num1, num2 = num2, num1
            n1, n2 = n2, n1

        res = [0] * n1
        upper = 0
        for i in xrange(n1 - 1, -1, -1):
            for j in xrange(n2 - 1, -1, -1):
                res[i] += int(num1[i]) * int(num2[j]) * pow(10, n2 - j - 1)
            tmp = (res[i] + upper) / 10
            res[i] = (res[i] + upper) % 10
            upper = tmp

        str_res = ""
        for item in res:
            str_res += str(item)
        if upper != 0:
            str_res = str(upper) + str_res

        return str_res
