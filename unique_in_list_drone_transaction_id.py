
data_list = []
for i in range(100):
    data_list.append(i)
    data_list.append(i)

data_list.remove(9)

def find_unique(delivery_list):
    result=0
    
    for item in delivery_list:
        result ^= item
        print(result)

    if result==0:
        raise AttributeError("No values are missing")
    return result
    
print(find_unique(data_list))
                           
