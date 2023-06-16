def distribution(T): #function definition
    for _ in range(T):
        N = int(input())  #getting input of candies
        
        #conditon Check
        if (N % 3) == 0:
            print("YES")
        else:
            print("NO")

T=int(input())
distribution(T)  #function call
