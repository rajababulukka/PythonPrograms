
cake_tuples = [(7,160), (3,90), (2,15)]
capacity    = 20

def max_duffel_bag_value(cake_tuples, capacity):
    maxValue = [0] * (capacity+1)
    print(maxValue)
    for current_capacity in range(1,capacity+1):
        
        max_value_for_current_capacity = 0
        for cake_weight,cakeprofit in cake_tuples:
            if cake_weight <= current_capacity:
                max_value_cake = cakeprofit+maxValue[current_capacity-cake_weight]
                max_value_for_current_capacity = max(max_value_cake,max_value_for_current_capacity)
        maxValue[current_capacity] = max_value_for_current_capacity
    print(maxValue)
    return maxValue[capacity]

cake_tuples = [(7,160), (3,90), (2,15)]
capacity    = 20

print(max_duffel_bag_value(cake_tuples, capacity))
