# Check if the number is power of 2.

def check(n):
    if n == 1:
        return 1
    elif n % 2 == 1:
        return 0
    else:
        return check(n/2)


print check(256)
