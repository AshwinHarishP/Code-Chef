def rank(T):
    for test_case in range(T):
        X = int(input())
    
        if X <= max_rank:
            print("YES")
        else:
            print("NO")
            
T = int(input())
max_rank = 10
rank(T)
