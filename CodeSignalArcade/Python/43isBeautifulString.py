def solution(inputString):
    myDict = {}
    total = 0
    prev = ''
    for c in string.ascii_lowercase:
        cCount = inputString.count(c)
        myDict[c] = cCount
        total += cCount
        if prev != '':
            if myDict[c] > myDict[prev]:
                return False
        if cCount == 0:
            print("total is",total)
            if total < len(inputString):
                return False
        prev = c
        
    
    return True
