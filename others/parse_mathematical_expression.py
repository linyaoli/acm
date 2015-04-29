# "1+2*3" => 7
# "12+3" => 15
# "1*2+3" => 5

def compute(input):
    stack = []
    op_stack = []
    print stack
    print op_stack
    for item in input:
        if item in ['+', '*']:
            op_stack.append(item)
        else:
            stack.append(int(item))
    while op_stack != []:
        op = op_stack.pop()
        if op == '+':
            m = stack.pop()
            n = stack.pop()
            num = m + n
            stack.append(num)
        elif op == '*':
            m = stack.pop()
            n = stack.pop()
            num = m * n
            stack.append(num)

    return stack[0]

#input = "12+3"

####1
def reverse_polish(input):
    list_input = []
    num = ""
    for i in xrange(len(input)):
        if input[i].isdigit():
            num += input[i]
        else:
            list_input.append(num)
            num = ''
            list_input.append(input[i])


    list_input.append(num)
    #reverse
#    for i in xrange(1, len(list_input), 2):
#        list_input[i], list_input[i+1] = list_input[i+1], list_input[i]
    return list_input

    ##skype?
def compute2(tokens):
    stack = []
    for token in tokens:
        k = token
        if token in ['+', '*']:
            m = stack.pop()
            n = stack.pop()
            if token == '+':
                k = m + n
            elif token == '*':
                k = m * n
        stack.append(int(k))

    return stack[0]

input = "12*3+4"
"""
print compute2(reverse_polish(input))
print reverse_polish("1+2*3")
print compute2(reverse_polish("1+2*3")) # 7
print compute2(reverse_polish("12+3")) # 15
print compute2(reverse_polish("1*2+3")) # 5
print compute2(reverse_polish("1*2*3+4")) # 10
print reverse_polish("1+2+3*4")
print compute2(reverse_polish("1+2+3*4")) # 15
"""
def cal(input):
    input_list = reverse_polish(input)
    i = 0
    while i < len(input_list):
        if input_list[i] == '*':
            val = int(input_list[i-1]) * int(input_list[i+1])
            input_list[i-1] = str(val)
            del input_list[i]
            del input_list[i]
        else:
            i += 1
    temp = input_list

    for i in xrange(1, len(temp), 2):
        temp[i], temp[i+1] = temp[i+1], temp[i]
    return temp

#print cal("1+2+3*4")

#print compute2(cal(input))
#print reverse_polish("1+2*3")
print compute2(cal("1+2*3")) # 7
print compute2(cal("12+3")) # 15
print compute2(cal("1*2+3")) # 5
print compute2(cal("1*2*3+4")) # 10
#print reverse_polish("1+2+3*4")
print compute2(cal("1+2+3*4")) # 15
