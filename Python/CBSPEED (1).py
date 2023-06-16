def prone_to_errors(X,Y):

    #condition check    
    if Y > X:
        return("YES")
    else:
        return("NO")
        
(X,Y) = map(int,input().split(" ")) #getting input
result = prone_to_errors(X,Y) #function call
print(result)