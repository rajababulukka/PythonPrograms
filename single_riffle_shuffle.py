def is_riffled_once(deck,half1,half2):
    for card in deck:
        if len(half1)!=0 and card==half1[0]:
            half1.pop(0)
        elif len(half2)!=0 and card==half2[0]:
            half2.pop(0)
        else:
            return False
    return True


deck=[1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
deck1=[6, 7, 8, 9, 0, 1, 2, 3, 4, 5]
half1=[1, 2, 3, 4, 5]
half2=[6, 7, 8, 9, 0]
print(is_riffled_once(deck,half1,half2))
print(is_riffled_once(deck1,half1,half2))
