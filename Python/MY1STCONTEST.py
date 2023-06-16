def rating():
    (N,A,B) = map(int,input().split(" "))
    made_submission = N - A
    rated_user = made_submission -B
    print(str(made_submission)+" "+str(rated_user))
    
rating()