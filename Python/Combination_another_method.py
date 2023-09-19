import itertools as it

list_ele = [1,2,3,4,5]

res = []
for i in range(len(list_ele)):
    combinations = list(it.combinations(list_ele, i))
    print(combinations)
    sum_of_ele =[]

    for j in range(len(combinations)):
        sum_of_ele.append(sum(combinations[j]))
    res.append(sum_of_ele)
    
    print(" ")
print(res)


