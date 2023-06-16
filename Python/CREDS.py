def credits(T):
    
    for test_case in range(T):
        
        X,Y,Z = map(int,input().split())    #getting input
        credit_points = ( 4*X + 2*Y +0*Z)   #formula
        print(credit_points)
        
T=int(input())
credits(T)  #function call