T = int(input())
for tc in range(T):
    (X,Y,A) = map(int,input().split(" "))
    
    if A >= X and A< Y:
        print("YES")
    else:
        print("NO")
    # TODO: write code...