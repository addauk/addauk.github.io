def solution(s1, s2):
    common = 0
    x = len(s2)
    for c in s1:
        s2 = s2.replace(c,"",1)
        if len(s2) < x:
            x = len(s2)
            common+=1
    return common

