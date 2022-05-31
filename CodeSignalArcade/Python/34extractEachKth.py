def solution(inputArray, k):

    outputArray = []
    i = 1
    for e in inputArray:
        if i % k != 0:
            outputArray.append(e)
        i +=1
    return outputArray
