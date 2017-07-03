def permutation(str_1):
    if len(str_1)<=1:
        return set([str_1])

    all_permutations=[]

    for i in range(len(str_1)):
        first=str_1[i]
        rest=str_1[:i]+str_1[i+1:]
        permutations=permutation(rest)
        for permute in permutations:
            all_permutations.append(first+permute)
    return set(all_permutations)

print(permutation("ab"))
print(permutation("abc"))
print(permutation("raja"))
