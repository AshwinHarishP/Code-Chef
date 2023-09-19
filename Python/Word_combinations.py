def combinations(s,st,res,temp):
    if len(temp) != 0:
        res.append(temp)

    for i in range(st,len(s)):
        combinations(s, i+1, res, temp+s[i])

    return res
res = combinations(input(), 0, [], 0)
print(res)
print(len(res))
