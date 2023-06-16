def information(T):
    for test_case in range(T):
        
        K,X = map(int,input().split())  #getting input
        K= K*7  #Since 1 week = 7 days
        
        get_information = K - X #formula
        print(get_information)


T=int(input())
information(T)

