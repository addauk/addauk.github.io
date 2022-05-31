def solution(name):
    letters = list(string.ascii_letters)
    letters.append("_")
    print(letters)
    if name[0] not in letters:
        return False
    letters = letters+list(string.digits)
    for x in range(1,len(name)):
        if name[x] not in letters:
            return False
    return True
