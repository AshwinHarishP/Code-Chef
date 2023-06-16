def buying_minimum_chairs(T):
    
    for test_case in range(T):
        X,Y = map(int,input().split())  #getting input
        
        minimum_chairs = X-Y    #formula
        
        #condition check
        if minimum_chairs < 0:  
            print("0")
        else:
            print(minimum_chairs)
            
T=int(input())            
buying_minimum_chairs(T)