#describe a number in english.
#19,323,984 -> nineteen million three hundred twenty two thousand nine hundred eighty two.
class Solution:
    def describe(self, number):
        millions = number / 10**6
        thousands = number % 10**6 / 10**3
        ret = ""
        if millions > 0:
            ret += self.getNumber(millions) + 'million '
        if thousands > 0:
            ret += self.getNumber(thousands) + 'thousand '

        ret += self.getNumber(number % 1000)
        return ret

    def getNumber(self, number):
        ret = ""
        if number >= 100:
            ret = self.getPhrase(0, number / 100) + self.getPhrase(3, 0)
            number = number % 100
        if number >= 20:
            ret += self.getPhrase(2, number / 10 - 1)
        elif number > 10 and number < 20:
            ret += self.getPhrase(1, number % 10)
        number %= 10
        if number > 0:
            ret += self.getPhrase(0, number)
        return ret


    def getPhrase(self, idx1, idx2):
        level = [['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'],
            ['eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen','nineteen'],
            ['ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety'],
            ['hundred', 'thousand', 'million']]

        return level[idx1][idx2] + ' '

sol = Solution()
#FIXME some bugs
# later.
print sol.describe(192323911)
