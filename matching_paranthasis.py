msg = "Sometimes (when I nest them (my parentheticals) too much (like this (and this))) they get confusing."

def find_close_paren(msg, start):
    if msg[start]!="(":
        raise Exception

    i = start
    end = len(msg)
    count=0
    while i<end:
        ch=msg[i]
        if ch=="(":
            count+=1
        elif ch==")":
            count-=1
            if count==0:
                return i
        i+=1
    return None

print(find_close_paren(msg,10))
