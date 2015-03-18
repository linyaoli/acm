def func(a):
    return a+10

def search(arr, x):
    s = 0
    e = len(arr) - 1
    while s <= e:
        mid = (s+e)/2
        if arr[mid] < x:
            s = mid + 1
        elif arr[mid] > x:
            e = mid - 1
        else:
            break

    return mid, arr[mid], x

a = [1,2,3,4,5,6]
print search(a, 2)
#print map(func, a)

def passbyreference(ref):
    ref.append(1)

ref = [1,2,3]
#passbyreference(ref)
#print ref

def passbyvalue(ref):
    reff = ref
    #reff = ref[:]
    reff.append(1)

passbyvalue(ref)
print ref

def func(n):
    if n < 10:
        print n,n+1,n+2
        func(n+3)


func(0)
