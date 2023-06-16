def donate_amount(T):
    
    for test_case in range(T):
        X,Y = map(int,input().split())   #getting input
        
        donated_amount = Y - X  #formula
        
        print(donated_amount)
        
        
T=int(input())
donate_amount(T)   #function call