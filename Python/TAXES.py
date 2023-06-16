def money(T):
    
    #getting input
    for test_case in range(T):
        X = int(input())
        
        #condition check
        if X <= 100:
            print(X)
        elif X > 100:
            tax= X - 10  #calculating tax
            print(tax)
            
T=int(input())
money(T)