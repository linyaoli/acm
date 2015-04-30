class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer
    def search(self, A, target):
        n = len(A)
        start = 0
        end = n - 1
        while start <= end:
            mid = (start + end) / 2
            if A[mid] == target:
                return mid

            if A[mid] >= A[start]:
                if A[mid] > target and target >= A[start]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                if A[mid] < target and target <= A[end]:
                    start = mid + 1
                else:
                    end = mid - 1

        return -1


sol = Solution()
print sol.search([5, 1, 3], 3)


class entryExit(object):
    def __init__(self, f):
        self.f = f
    def __call__(self):
        print "Entering", self.f.__name__
        self.f()
        print "Exited", self.f.__name__

@entryExit
def func1():
    print "inside func1"
@entryExit
def func2():
    print "inside func2"

func1()
func2()
print "---------------"
def entryExit(f):
    def new_f():
        print "Entering", f.__name__
        f()
        print "Exited", f.__name__
    return new_f

@entryExit
def func1():
    print "inside func1()"

@entryExit
def func2():
    print "inside func2()"

func1()
func2()
print func1.__name__
print func2.__name__
