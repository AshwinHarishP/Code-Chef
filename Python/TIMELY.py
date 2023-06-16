def on_time(T):
    
    for _ in range(T):
        X = int(input()) #getting input
        time = X-30 #formula

        #condition
        if time < 0:
            print("NO")
        else:
            print("YES")
            
T=int(input())
on_time(T)