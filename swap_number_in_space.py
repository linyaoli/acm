def swap(a, b):
    a = a - b
    b = a + b
    a = b - a
    print a, b
    a = a^b
    b = a^b
    a = a^b
    print a, b


swap(2, 7)
