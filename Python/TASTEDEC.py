def purchase(T):
    
    for test_case in range(T):
        
        X,Y = map(int,input().split())  #getting input

        #formula
        choculate_taste= 2*X
        candy_taste= 5*Y
        
        #Condition check
        if choculate_taste>candy_taste:
            print("Chocolate")
        elif choculate_taste<candy_taste:
            print("Candy")
        else:
            print("Either")
            
T=int(input())
purchase(T)
