# given a list, print all even numbers with even indices.
def even(input):
    #[i:j:k], get from [i, j), step = k
    return [x for x in input[::2] if x % 2 == 0]

# what will be the outputs?
def extendList(val, x=[]):
    x.append(val)
    print x

#extendList(10) -> [10]
#extendList(100, []) -> [100]
#extendList(12) -> [10, 12]

# what will be the output of the code below? explain the answer.
class Parent(object):
    x = 1
class Child1(Parent):
    pass
class Child2(Parent):
    pass
#print Parent.x, Child1.x, Child2.x
Child1.x = 2
#print Parent.x, Child1.x, Child2.x
Parent.x = 3
#print Parent.x, Child1.x, Child2.x

#what will be the output of the code below? Explain your answer.
def multipliers():
    return [lambda x : i * x for i in [1,3,5]]
#TODO why? [10, 10, 10]
# python's closure are late bindings. this means that the values of variables used in closures are
# looked up at the time the inner function is called.
#print [m(2) for m in multipliers()]

# consider the following snippets
# TODO this line creates five copies of one single list, which all refer to the same object.
x = [[]]*5
#print list
x[0].append(10)
#print list
x[1].append(20)
#print list
x.append(10)
#print list
def create_multipliers():
    multipliers = []
    for i in range(5):
        def multiplier(x):
            return i * x
        multipliers.append(multiplier)
    return multiplier

def create_multipliers():
    return [lambda x, i = i : i * x for i in range(5)]

#why use function decorators?
#TODO allows code reuse and reduce redundant code.

#lambda
#TODO concise code.

#filter(func, iterable), map, reduce
#filter: apply a function in an iterable object, and return all those items whose return value
# is True(only for return value is True/False).
def func(i):
    if i % 2 == 1:
        return True
print map(func, [1,2,3,4])
# map: apply a function in an iterable object and return all results.
# reduce(function, sequence, starting_value):apply function in sequence, if there is a starting value,
# it can be used for intialization.

#############################################
#
#
#############################################
# if we have an unknown function:
#for x in f(5):
#    print x,
# output: 0 1 8 27 64
# implement f.
def f(n):
    for x in range(n):
        yield x**3

#print f(5)
#for x in f(5):
    #print x,

####
#Build a string with the numbers from 0 to 100, "0123456789101112..."
''.join(`x` for x in xrange(101)) # `x` is equal to str(x)

try:
    with open('atoi.c', 'r') as f:
        content = f.read()
except IOError:
    pass
    #print 'No such file exists'
# monkey patching
######
# remove dups
dup_list = [1,2,3,4,4,4,5,1,2,7,8,8,10]
unique_list = list(set(dup_list))
#print unique_list

# regarding the underlines
# _func(), referred as the private function, cannot be accessed outside.
# func_, used to distinguish from built-in functions, e.g. list_ -> list
# __func, if this function is in class Test, when use dir(Test), you will see _Test__func.
# __init__, __del__, __add__, __getitem__

#read lines from file
#with open('atoi.c') as f:
#    content = f.readlines()
#content = [x.strip('\n') for x in content]
#content = content.split('\n')
#print content
#f.close()
#print ''.join(content)
#with open('test.io.py', 'w+') as f:
#    f.write(''.join(content))
class test:
    def __enter__(self):
        print 'in enter'
    def __exit__(self, type, value, traceback):
        print 'in exit'

with test() as t:
    print 'a'

class test1:
    def __init__(self):
        pass
    def f(self):
        print 'test1'
class test2:
    def __init__(self):
        pass
    def f(self):
        print 'test2'

class test3(test2, test1):
    def __init__(self):
        pass
#    def f(self):
#        print 'test3'

t = test3()
t.f()

def tester(a, b):
    def tester1(a=a, b=b):
        return a, b
    return tester1

tester1 = tester(10, 20)
print tester1.func_closure

def bread(func):
    def wrapper():
        print "</''''''\>"
        k = func()
        print k
        print "<\______/>"
        return '111'
    return wrapper

@bread
def haha():
    print 'haha'
    return '222'

a = haha()
print a
