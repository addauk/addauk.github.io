def solution(inputArray):
    inputArray.sort()
    top = inputArray[-1]
    jump = 1
    pos = 0
    while True:    
        if pos > top:
            return jump    
            
        if pos in inputArray:
            pos = 0
            jump += 1
        else:
            pos += jump 
            
