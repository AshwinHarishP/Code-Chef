def ability_to_ride(T):
    
    for _ in range(T):
        (X,H) = map(int,input().split(" ")) #getting input
         
        #condition check
        if X < H:
            print("NO")
        else:
            print("YES")
            
T=int(input())
ability_to_ride(T) #function call