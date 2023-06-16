def Total_amount(T):
    
    for test_case in range(T):
        (X,Y) = map(int,input().split(" "))
        pay = X * Y
        print(pay)


T = int(input())
Total_amount(T)    
    
