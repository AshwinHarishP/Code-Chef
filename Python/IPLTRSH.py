def wont_able_to_book(T):
    
    #getting input
    for test_case in range(T):
        (N,M) = map(int,input().split(" "))
        
        #formula
        tickets = N-M
        
        #condition check
        if tickets<0:
            print("0")
        else:
            print(tickets)
            
            
T=int(input())            
wont_able_to_book(T)
