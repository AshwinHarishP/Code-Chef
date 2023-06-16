def check_answer(T):
    for test_case in range(T):
        A,B,C = map(int,input().split())    #getting input
        
        #Condition check
        if A+B==C:
            print("YES")
        else:
            print("NO")


T=int(input())
check_answer(T)     #function call       