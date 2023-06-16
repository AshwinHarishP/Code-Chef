def Max_people(T):
    
    for _ in range(T):
        (N,M) = map(int,input().split(" ")) #getting input
        people_can_travel = (N*5) + (M*7) #formula
        print(people_can_travel)
         
         
T=int(input())
Max_people(T)