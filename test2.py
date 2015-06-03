str1 = "123456789 123456789 123456789 123456789"
idx = 0
mark = 0
size = 11
out = []
for i in xrange(len(str1)):
    if str1[i] == ' ':
        if i % size != 0:
            mark = 1
        else:
            out.append((i-size, size))
    else:
        if i % size == 0:
            if mark == 1:
                out.append((i-size, size))
                mark = 0
            else:
                pass
if i % size != 0:
    out.append((i-i%size, i % size))
print out
