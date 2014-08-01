class Solution:
    # @return a list of lists of string
    def solveNQueens(self, n):
        rows = [0]*n
        res = []
        self.gen(n, 0, rows, res)
        return res

    def gen(self, n, row, rows, res):
        if row == n:
            item = []
            for i in xrange(n):
                tmp = ""
                for j in xrange(n):
                    if rows[i] == j:
                        tmp += 'Q'
                    else:
                        tmp += '.'
                item.append(tmp)
            res.append(item)
        else:
            for i in xrange(n):
                rows[row] = i
                if self.check(row, rows):
                    self.gen(n, row + 1, rows, res)

    def check(self, row, rows):
        for i in xrange(row):
            if rows[i] == rows[row] or abs(rows[row] - rows[i]) == row - i:
                return False
        return True
