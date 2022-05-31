def solution(sequence):
    moves = 0
    
    for i in range(1,len(sequence)):
        if sequence[i] <= sequence[i - 1]:
            #we've hit a problem index
            dif = sequence[i - 1] - sequence[i] + 1
            sequence[i] += dif
            moves += dif  
    return moves


