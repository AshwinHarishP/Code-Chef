n = int(input())
i = 2
while(n != 1):
    con = 0
    while(n % i == 0):
        n //= i
        con += 1

    if con > 0: 
        print(i, con)
    i += 1
