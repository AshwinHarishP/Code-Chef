def equal_number_of_choculates(T):
    for _ in range(T):
        N = int(input()) #getting input

        #condition check        
        if(N % 2) == 0:
            print("YES")
        else:
            print("NO")
            
T=int(input())
equal_number_of_choculates(T) #function call