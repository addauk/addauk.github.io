def solution(inputString):
    
    return splitSwap(inputString)


def splitSwap(string):
    
        if string.__contains__("("):
            l = string.rfind("(")
            left = string[:l]
            r = string.find(")",l+1)
            right = string[r+1:]
            mid = "".join(reversed(string[l+1:r]))
            return splitSwap(left+mid+right)
        else:
            return string   
    
    
    