def solution(a):
    
    b = sorted([x for x in a if x != -1],reverse=True)
    print(b)
    for i in range(len(a)):
        if a[i] != -1:
            a[i] = b.pop()
            
    
    return a
    


