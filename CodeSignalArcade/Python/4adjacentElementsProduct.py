def solution(inputArray):
    maxAdj = inputArray[0] * inputArray[1]
    
    for i in range(1,len(inputArray) - 1):
        
        adj = inputArray[i] * inputArray[i+1]
        if adj > maxAdj:
            maxAdj = adj
        
            
    return maxAdj
    

