import random

def rand5():
    return random.choice([1,2,3,4,5])
   

def rand7():
    while True:
        val1=5*(rand5()-1)
        print("Val1:",val1)
        val2=rand5()
        print("Val2:",val2)
        val=val1+val2
        if val <=21:
            return val%7+1

print(rand7())
