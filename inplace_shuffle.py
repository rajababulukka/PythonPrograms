import random

def get_random(floor, ceiling):
    return random.choice(range(floor,ceiling+1))

def shuffle(arr):
    if len(arr)<=1:
        return arr
    for index in range(len(arr)):
        swap_index = get_random(index,len(arr)-1)
        arr[index], arr[swap_index] = arr[swap_index],arr[index]
    return arr

arr=[1,2,3,4,5]

print(shuffle(arr))
print(shuffle(arr))
