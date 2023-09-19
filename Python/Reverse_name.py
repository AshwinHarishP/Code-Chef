def reverse(s,tp):
    if len(s) == tp:
        return
    
    reverse(s, tp+1)
    print(s[tp])
reverse(input(), 0)
    
