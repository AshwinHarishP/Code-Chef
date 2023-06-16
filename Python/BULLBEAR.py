def pofit_or_not(T):

    for test_case in range(T):
        (X,Y) = map(int,input().split(" "))  #getting input

        #condition check        
        if X < Y:
            print("PROFIT")
        elif X > Y:
            print("LOSS")
        else:
            print("NEUTRAL")

T=int(input())
pofit_or_not(T)  #function call