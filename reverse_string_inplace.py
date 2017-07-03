def string_reverse(string):
    b = bytearray(string, 'utf8')
    b = reverse_byte_in_place(b)

    return str(b)

def reverse_byte_in_place(list_1):
    n = len(list_1)
    print("length:",n)
    for i in range(int(n/2)):
        [list_1[i],list_1[n-i-1]] = [list_1[n-i-1],list_1[i]]
    return list_1

name = list("rajababu")
print(reverse_byte_in_place(name))         
