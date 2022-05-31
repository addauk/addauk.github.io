def solution(inputString):
    newStr = ""
    for c in inputString:
        if c in string.digits:
            newStr += c
        else:
            return newStr
    return newStr

