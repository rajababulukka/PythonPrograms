def valid_brackets(msg):
    brackets=[]
    bracket_map={'(':0,'{':0,'[':0,')':'(','}':'{',']':'['}
    for ch in msg:
        if ch in bracket_map:
            brack = bracket_map[ch]
            if brack==0:
                brackets.append(ch)
            else:
                if len(brackets)<=0:
                    return False
                top=brackets.pop()
                if brack!=top:
                    return False
    if len(brackets)==0:
        return True
    return False

print("{ [ ] ( ) }:",valid_brackets("{ [ ] ( ) }"))
print("{ [ ( ] ) }:",valid_brackets("{ [ ( ] ) }"))
print("{ [ }:",valid_brackets("{ [ }"))
