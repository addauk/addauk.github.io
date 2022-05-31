def solution(picture):
    c = len(picture[0])+2
    top = "*"*c
    border = [top]
    for elem in picture:
        border.append("*"+elem+"*")
    border.append(top)
    return border

