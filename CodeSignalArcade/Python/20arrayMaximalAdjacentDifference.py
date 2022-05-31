def solution(inputArray):
    maxd = 0
    for i in range(len(inputArray)-1):
        dif = abs(inputArray[i] - inputArray[i+1])
        if dif > maxd:
            maxd=dif
    return maxd
            
        
        

