def get_products_of_all_ints_except_at_index(listnew):
    products_at_index = [None]*len(listnew)
    print(products_at_index)

    product_current = 1
    i=0
    while i < len(listnew):
        products_at_index[i] = product_current
        print("current product", product_current)
        print(products_at_index)
        product_current *= listnew[i]
        print("list element", listnew[i])
        i+=1
    print(products_at_index)
        
    product_current = 1
    i=len(listnew) - 1
    while i>=0:
        print(" product at index",  products_at_index[i])
        products_at_index[i] *= product_current
        print("current product", product_current)
        print(products_at_index)
        product_current *= listnew[i]
        print("list element", listnew[i])
        i-=1

    print(products_at_index)
    return products_at_index

listone = [1,7,3,4]
get_products_of_all_ints_except_at_index(listone)
