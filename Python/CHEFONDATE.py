def money(T):
    
    for _ in range(T):
        X,Y =map(int,input().split(" ")) #getting input
        
        #condition check
        if X < Y:
            print("NO")
        else:
            print("YES")
            
T=int(input())
money(T) #function call