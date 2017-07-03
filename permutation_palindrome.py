def palindrome(str_1):
    freq={}
    for ch in str_1:
        if ch in freq:
            del freq[ch]
        else:
            freq[ch]=True
    return len(freq)<=1

print(palindrome("civic"))
print(palindrome("ivicc"))
print(palindrome("civil"))
print(palindrome("livci"))
