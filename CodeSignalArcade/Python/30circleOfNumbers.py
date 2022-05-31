def solution(n, firstNumber):
    place = firstNumber - n/2
    if place < 0:
        place = n+place
    return place
