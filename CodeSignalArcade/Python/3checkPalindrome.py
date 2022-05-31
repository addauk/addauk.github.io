def solution(inputString):
    palin = True
    compstring = inputString[::-1]
    
    for (x,y) in zip(compstring,inputString):
        if x != y:
            palin = False
    
    return palin

