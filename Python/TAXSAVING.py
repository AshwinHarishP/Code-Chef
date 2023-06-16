def Tax(T):
    for test_case in range(T):
        (X,Y)=map(int,input().split(" "))
        tax= X-Y
        print(tax)
    
    
T=int(input())
Tax(T)
