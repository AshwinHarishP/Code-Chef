def final_score(t):
    
    for i in range(t):
        X,Y = map(int,input().split()) #getting input
        print(max(X,Y))
        
t = int(input())
final_score(t)