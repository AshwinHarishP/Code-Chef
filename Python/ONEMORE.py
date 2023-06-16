def new_episode(T):
    for test_case in range(T):  
        X=int(input())  #getting input
        
        #checking condition
        if X > 24:
            print("YES")
        else:
            print("NO")
        
T=int(input())            
new_episode(T)  #function call