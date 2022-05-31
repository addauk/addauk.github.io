def solution(inputArray, k):
    
    maxS = sum(inputArray[0:k])
    new = sum(inputArray[0:k])
    for i in range(len(inputArray)-k):
        new = new - inputArray[i] + inputArray[i+k]
        maxS = max(new,maxS)
    return maxS

