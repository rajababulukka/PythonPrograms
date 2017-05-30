

def list_of_coins(amount, demons):
    ways_of_doing_n_cents = [0]*(amount+1)
    ways_of_doing_n_cents[0] = 1

    for coin in demons:
        print("coin",coin)
        for high_amount in range(coin,amount+1):
            print("high_amount",high_amount)
            remainder = high_amount - coin
            print("remainder",remainder)
            ways_of_doing_n_cents[high_amount] += ways_of_doing_n_cents[remainder]
            print("list",ways_of_doing_n_cents)
            print("amount at index",ways_of_doing_n_cents[high_amount]) 
        
    print("no.of solutions: ",ways_of_doing_n_cents[amount])            
    return ways_of_doing_n_cents[amount]

    

denominations = [1,2,3]
amt = int(input("Enter amount:"))
list_of_coins(amt,denominations)
