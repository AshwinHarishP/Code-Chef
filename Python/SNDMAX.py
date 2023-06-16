def second_maximum(N):
    for _ in range(N):
        List_a = [] #creating list
        a,b,c = map(int,input().split()) #getting input
    
        List_a.append(a)
        List_a.append(b)    #adding values in list
        List_a.append(c)

        new_list=sorted(List_a,reverse=True) #sorting in decending order
        
        print(new_list[1])  #accessing second element in list   

N=int(input())

second_maximum(N)