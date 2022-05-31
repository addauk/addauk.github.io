def solution(n):
    strnum = str(n)
    length = len(strnum)//2
    left = 0
    right = 0
    half1, half2 = strnum[:length],strnum[length:]
    for i in range(length):
        left += int(half1[i])
        right += int(half2[i])
        
    
    if left == right:
        return True
    else:
        return False
