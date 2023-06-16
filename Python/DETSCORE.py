def score(T):
    for test_case in range(T):
        (X,N) = map(int,input().split(" "))
        
        if N!= 0:
            points = (X*N)//10
            print(points)
        else:
            print("0")
        
        
T = int(input())
score(T)
