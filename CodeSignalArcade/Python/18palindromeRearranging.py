def solution(inputString):
    odd = 0
    while inputString != "":
        cur = inputString[0]
        x = inputString.count(cur)
        inputString = inputString.replace(cur,"")
        if x % 2 == 1:
            odd += 1
            
    if odd >1:
        return False
    else:
        return True

