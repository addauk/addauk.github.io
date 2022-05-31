def solution(inputString):
    outputString = ""
    for x in inputString:
        a = ord(x)
        if a == 122:
            a = 97
        else:
            a += 1
        outputString += chr(a)
    return outputString