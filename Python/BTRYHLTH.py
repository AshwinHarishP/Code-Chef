def optimal_condition(T):
    for test_case in range(T):  
        X = int(input())   #getting input
        
        #condition check
        if X < 80:
            print("NO")
        else:
            print("YES")
            
            
T = int(input())
optimal_condition(T)  #function call