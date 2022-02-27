def get_list_0s(num):
    retval = []
    for val in range(num):
        retval.append("0")
    return retval

def alu(x, y):
    retval = get_list_0s(len(x))
    carry = 0
    for i in range(len(x)-1, -1, -1):
        b1 = int(x[i])
        b2 = int(y[i])
        op = b1 + b2 + carry
        if op == 2:
            carry = 1
            op = 0
        elif op == 3:
            carry = 1
            op = 1
        else:
            carry = 0
        retval[i] = str(op)
    return ''.join(retval)

def reverse(x):
    retval = get_list_0s(len(x))
    for i in range(len(x)-1, -1, -1):
        if x[i] == "0":
            retval[i] = "1"
        elif x[i] == "1":
            retval[i] = "0"
    return ''.join(retval)

def get_negative_complement(x):
    y = reverse(x)
    return alu(y, "00000001")

def get_positive_complement(x):
    y = alu(x, "11111111")
    return reverse(y)

def check_10000000(x):
    if x[0] == "1":
        for i in range(1,len(x)):
            if x[i] == "1":
                return 0
    else:
        return 0
    return -1 * unsigned_binary_to_number(x)

def unsigned_binary_to_number(binary):
    binary = binary[::-1]
    val = 0
    for i in range(0, len(binary)):
        val += int(binary[i]) * 2**(i)
    return val

def signed_binary_to_number(binary):
    check = check_10000000(binary)
    if check != 0:
        return check
    lead = binary[0]
    symbol =  1
    val = binary[1:]
    if lead == "1":
        symbol = -1
        val = get_positive_complement(val)
    return unsigned_binary_to_number(val) * symbol

def signed_number_to_binary(x):
    pass

def sign_extension(x, k):
    vals_to_add = k - len(x)
    fill = x[0]
    additive = []
    for i in range(vals_to_add):
        additive.append(fill)
    return ''.join(additive) + x

#x = "01000000"
#print(signed_binary_to_number(x))

x = "101"
print(sign_extension(x, 8))