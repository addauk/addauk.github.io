def solution(n):
    count = 0
    while digitCount(n) > 1:
        n = sumDigits(n)
        count +=1
        
    return count
    

def sumDigits(n):
    total = 0
    n = str(n)
    for x in n:
        total += int(x)
    return total

def digitCount(n):
    import math
    if n > 0:
        digits = int(math.log10(n))+1
    elif n == 0:
        digits = 1
    else:
        digits = int(math.log10(-n))+2
    return digits