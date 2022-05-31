def solution(a):
    labs = {}
    for x in a:
        total = 0
        for y in a:
            total += abs(y-x)
        labs[x] = total
    return min(labs, key=labs.get)

