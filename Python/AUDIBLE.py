def binary(T):
    
    for i in range(T):
        hertz = int(input()) #getting input
        
        #condition check
        if (hertz >= max_hertz_1) and (hertz <= max_hertz_2):
            print("YES")
        else:
            print("NO")
            
T=int(input())    
max_hertz_1 = int(67)
max_hertz_2 = int(45000) 

binary(T)