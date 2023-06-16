def Total_prize(T):
    for _ in range(T):
        
        (X,Y) = map(int,input().split(" ")) #getting input
        prize = (10*X) +(90*Y) #formula
        print(prize)

T=int(input())        
Total_prize(T) #function call
