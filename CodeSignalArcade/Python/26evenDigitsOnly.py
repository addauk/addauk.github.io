def solution(n):
    strnum = str(n)
    for x in strnum:
        if int(x)%2 == 1:
            return False

    return True