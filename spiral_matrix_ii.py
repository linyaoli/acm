class Solution:
    # @return a list of lists of integer
    def generateMatrix(self, n):
        res = []
        for i in xrange(n):
          res.append([0] * n)
        self.gen(res, 0, n, 0, n, 0)
        return res
    def gen(self, res, row_s, row_len, col_s, col_len, val) :
        if row_len <= 0 or col_len <= 0:
            return
        if row_len == 1:
            for i in xrange(col_s, col_s + col_len, 1):
                val += 1
                res[row_s][i] = val
            return
        if col_len == 1:
            for i in xrange(row_s, row_s + row_len, 1):
                val += 1
                res[i][col_s] = val
            return
        for i in xrange(col_s, col_s + col_len - 1, 1):
            val += 1
            res[row_s][i] = val
        for i in xrange(row_s, row_s + row_len - 1, 1):
            val += 1
            res[i][col_s + col_len - 1] = val
        for i in xrange(col_s, col_s + col_len - 1, 1):
            val += 1
            res[row_s + row_len - 1][2 * col_s + col_len - 1 - i] = val
        for i in xrange(row_s, row_s + row_len - 1, 1):
            val += 1
            res[2 * row_s + row_len - 1 - i][col_s] = val
        self.gen(res, row_s + 1, row_len - 2, col_s + 1, col_len - 2, val)

                
