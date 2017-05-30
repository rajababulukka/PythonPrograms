import itertools
from itertools import islice
#import operators


def meeting_times(tup_list):
    list_stack=[]
    sorted_elements = sorted(tup_list, key=lambda tup: tup[0])
    print(sorted_elements)
    list_stack.append(sorted_elements[0])

    
    for ele in itertools.islice(sorted_elements,1,None):
        print("stack:",list_stack)
        print("element:",ele)
        print("comp1:",list_stack[-1][1])
        print("comp2:",ele[0])
        if list_stack[-1][1] < ele[0]:
            print("element:",ele)
            list_stack.append(ele)
        elif list_stack[-1][1] < ele[1]:
            top = (list_stack[-1][0],ele[1])
            list_stack.pop()
            list_stack.append(top)

    print(list_stack)
    return list_stack
            








list_tupples =   [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
meeting_times(list_tupples)
