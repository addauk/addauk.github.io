def solution(cell1, cell2):
    return blackCheck(cell1) == blackCheck(cell2)
    


def blackCheck(cell):
    #letter and number both odd or even
    if ord(cell[0]) %2 == int(cell[1])%2:
        return True
    else:
        return False
    

