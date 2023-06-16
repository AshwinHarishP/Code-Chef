def memory(T):
    
    for test_case in range(T):
        N,X,Y = map(int,input().split())    #getting input
        
        memory_space = X + (Y*2)  #formula
        
        #condition check
        if memory_space>N:
            print("NO")
        else:
            print("YES")
            
            
T = int(input())
memory(T)   #function call