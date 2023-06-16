def special_attacks(T):
    
    for test_case in range(T):
        X,Y = map(int,input().split())  #getting input
        print(Y//X)
            
T = int(input())
special_attacks(T)    #function call