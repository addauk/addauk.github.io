def solution(deposit, rate, threshold):
    year = 0
    rate = rate/100
    while deposit < threshold:
        deposit += deposit * rate
        year += 1
    return year

