def runs_needed(T):
    
    for _ in range(T):
        (X,Y) = map(int,input().split(" ")) #getting inputs
        required_runs = X - Y #formula
        print(required_runs) 

T=int(input())
runs_needed(T)