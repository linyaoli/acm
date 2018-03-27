"""
Question:
The API: int read4(char *buf) reads 4 characters at a time from a file.
The return value is the actual number of characters read. For example, it returns 3 if there
is only 3 characters left in the file.
By using the read4 API, implement the function int read(char *buf, int n) that reads n characters from the file.
Note: The read function will only be called once for each test case.

"""
class Solution:
    def read4(self, buf):
        # read 4 chars
        n = len(buf)
        return n

    def read(self, buf, n):
        msg = []
        ret = []
        a = n / 4
        if n % 4 != 0:
            a += 1
        for i in xrange(a):
            read4(msg)
            ret.append(msg)
