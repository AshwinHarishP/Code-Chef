def check_host_part(T):
    for test_case in range(T):
        (N,M) = map(int,input().split(" "))     #getting input
        
        #condition check
        if N>M:
            print("NO")   
        else:
            print("YES")
            
T=int(input())
check_host_part(T)