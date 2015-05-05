def is_prime(n):
    if n == 2:
        return True
    if (n < 2) or (n % 2 == 0):
        return False
    return all(n % i for i in range(3, int(sqrt(n)) + 1, 2))
    # Return True if bool(x) is True for all values x in the iterable.
    # If the iterable is empty, return True.

def next_prime(n):
    if n < 2:
        return 2
    if is_prime(n): # prevent return n if n is prime
        n += 1
    if (n % 2 == 0) and (n != 2):
        n += 1
    while True:
        if is_prime(n):
            break
        n += 2
    return n
