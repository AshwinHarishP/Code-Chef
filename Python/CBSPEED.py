def prone_to_errors():
    (X,Y) = map(int,input().split(" ")) #getting input

    #condition check    
    if Y > X:
        print("YES")
    else:
        print("NO")
        
prone_to_errors()