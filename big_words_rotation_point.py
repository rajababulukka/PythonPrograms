words = [
    'ptolemaic',
    'retrograde',
    'supplant',
    'undulate',
    'xenoepist',
    'asymptote', # <-- rotates here!
    'babka',
    'banoffee',
    'engender',
    'karpatka',
    'othellolagkage',
]


def rotate(words):
    min_1=0
    max_1 = len(words)
    print("first max:", max_1)
    first = words[0]

    while(min_1 < max_1):
        pivot = int((min_1+max_1)/2)
        print("Pivot",pivot)
        if (words[pivot] < first):
            max_1 = pivot-1
            print("max:", max_1)
        else:
            min_1 = pivot+1
            print("min:", min_1)
            print("max:", max_1)

        if min_1==max_1:
            print("max==min:", max_1,min_1)
            return max_1
    return min_1
    

print(rotate(words))
