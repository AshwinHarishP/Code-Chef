def hours(T):
    for test_case in range(T):
        (X,Y) = map(int,input().split(" "))
        
        hours_of_work = Y-X
        print(hours_of_work)
        
        
T = int(input())
hours(T)