from itertools import islice


def highest_product_of_3(listnew):
    if len(listnew)<3:
        raise Exception("List consists less than 3 items")

    max_product = max(listints[0],listints[1])
    min_product = min(listints[0],listints[1])
    max2_product = listints[0]*listints[1]
    min2_product = listints[0]*listints[1]
    max3_product = listints[0]*listints[1]*listints[2]

    for cur_val in islice(listnew,2,None):
        max3_product = max(max3_product, cur_val*max2_product, cur_val*min2_product)
        max2_product = max(max2_product, cur_val*max_product, cur_val*min_product)
        max_product = max(max_product,cur_val)
        min_product = min(max_product,cur_val)

    print(max3_product)
    return max3_product

listints = [3,5,2,4,9]

#listints.sort()
#print(listints[-1]*listints[-2]*listints[-3])
highest_product_of_3(listints)


