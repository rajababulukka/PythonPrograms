def sort_scores(unsorted_scores, HIGHEST_POSSIBLE_SCORE):
    count={}
    for x in unsorted_scores:
        score=count.get(x,0)
        count[x]=score+1

    sorts=[]
    for i in range(HIGHEST_POSSIBLE_SCORE+1):
        if i in count:
            aa = [i]*count[i]
            sorts.extend(aa)
    
    return sorts
    

unsorted_scores = [37, 89, 41, 65, 91, 53]
HIGHEST_POSSIBLE_SCORE = 100

print(sort_scores(unsorted_scores, HIGHEST_POSSIBLE_SCORE))
