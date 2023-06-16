def ML(T):
    
    for test_case in range(T):
        X = int(input())     
        
        if X < minimum_liter:
            print("NO")
        else:
            print("YES")
    
T = int(input())
minimum_liter = 2000
ML(T)