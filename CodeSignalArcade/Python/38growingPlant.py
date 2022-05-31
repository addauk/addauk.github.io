def solution(upSpeed, downSpeed, desiredHeight):
    currentHeight = 0
    days = 1
    while currentHeight <= desiredHeight:
        currentHeight += upSpeed
        if currentHeight >= desiredHeight:
            return days
        else:
            days +=1
            currentHeight-=downSpeed
    return days

