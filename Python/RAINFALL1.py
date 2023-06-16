def rainfall(T):
    for test_case in range(T):
        X = int(input())    #getting input
    
        #Condition check        
        if X < 3:
            print("LIGHT")
        elif X >= 3 and X < 7:
            print("MODERATE")
        else:
            print("HEAVY")
           
T=int(input())            
rainfall(T)    #Function call