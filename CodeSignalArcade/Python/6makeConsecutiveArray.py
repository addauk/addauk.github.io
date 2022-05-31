def solution(statues):
    myStat = sorted(statues)
    count = 0
    for i in range(len(myStat)-1):
        
        dif = myStat[i+1] - myStat[i]
        print("dif is", dif)
        if dif>1:
            count = count + dif - 1
    return count
        
        
        
    

