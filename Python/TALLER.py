def taller(T):
    
    for _ in range(T):
        (X,Y)=map(int,input().split(" ")) #getting input

        #condiotion check        
        if X<Y:
            print("B")
        else:
            print("A")
            
T=int(input())
taller(T)