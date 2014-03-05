
v1 = "10.33.2.1"
v2 = "10.33.2.1"

v1_list = v1.split('.')
v2_list = v2.split('.')
length = 0
print v1_list
if len(v1_list) < len(v2_list):
    length = len(v1_list)
else:
    length = len(v2_list)
flag = 0
for i in range(0, length, 1):
    if v1_list[i] < v2_list[i]:
        flag = 1
        print 1
        break
    elif v1_list[i] > v2_list[i]:
        flag = -1
        print -1
        break

if flag == 0:
    if len(v1_list) == len(v2_list):
        print 0
