T=int(input())
for test_case in range(T):
    (X,Y)=map(int,input().split(" "))
    Sum=X+Y
    
    if Sum <7:
        print("NO")
    else:
        print("YES")