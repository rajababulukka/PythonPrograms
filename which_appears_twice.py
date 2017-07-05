def which_appears_twice(l):
    n=len(l)
    guess=int((n-1)*(n/2.0))
    total=sum(l)
    duplicate=total-guess
    return duplicate


l = [3,1,2,3]
print(which_appears_twice(l))
