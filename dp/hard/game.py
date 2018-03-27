#Q1

def solution(n1, n2, k1, k2):
    min_times1 = min_times2 = 0
    if n1 <= k1:
        min_times1 = 1
    else:
        if n1 % k1 == 0:
            min_times1 = n1 / k1
        else:
            min_times1 = n1 / k1 + 1

    if n2 <= k2:
        min_times2 = 1
    else:
        if n2 % k2 == 0:
            min_times2 = n2 / k2
        else:
            min_times2 = n2 / k2 + 1
    print min_times1, min_times2
    if min_times1 <= min_times2 + 1:
        return "First"
    else:
        return "Second"


a = raw_input("")
a = a.split(" ")
print solution(int(a[0]), int(a[1]), int(a[2]), int(a[3]))
