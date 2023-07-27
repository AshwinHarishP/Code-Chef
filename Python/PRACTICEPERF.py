inputs = input().split()
count = 0
for i in inputs:
    if int(i) >= 10:
        count+=1
        
print(count)