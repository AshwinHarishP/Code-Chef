def concert(T):
    for test_case in range(T):
        X = int(input()) #getting input
        
        cost = 4*X   #Formula
        
        #condition check
        if cost<=1000:
            print("YES")
        else:
            print("NO")

            
T=int(input())
concert(T)  #function call
