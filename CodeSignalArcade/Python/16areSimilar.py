def solution(a, b):
    if a != b:
        i = 0
        while i < len(a):
            if a[i] == b[i]:
                a.pop(i)
                b.pop(i)
            else:
                i += 1
                
        if len(a) !=2:
            return False
        
        if a[::-1]==b:
            return True
        else:       
            return False
    return True
        

