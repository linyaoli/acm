fibos = [1, 1, 2, 3, 5]
while fibos[-1] < 10 ** 10:
    fibos.append(fibos[-1] + fibos[-2])
