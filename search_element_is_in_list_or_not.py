gas_prices = []

gas_prices.append(346)
gas_prices.append(360)
gas_prices.append(354)

def find(n):
    flag=0
    for i in gas_prices:
        if n==i:
            flag=1
         
    if flag==1:
        print("Number is in list")
    else:
        print("Not in list")
        

n = int(input("enter a number:"))
find(n)
