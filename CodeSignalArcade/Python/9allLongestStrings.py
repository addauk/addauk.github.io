def solution(inputArray):
    
    biggest = len(max(inputArray,key = len))
    return [x for x in inputArray if len(x) == biggest]
    
    

