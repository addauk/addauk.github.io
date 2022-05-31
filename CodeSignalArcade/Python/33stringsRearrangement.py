import itertools

def solution(inputArray):
        
    perms = list(itertools.permutations(inputArray))
    #iterate over all permutations
    for p in perms:
        found = True
        #iterate over a single permutation
        for x in range(len(p)-1):
            diff = 0
            #iterate over a single word
            for a,b in zip(p[x],p[x+1]):
                if a != b:
                    diff +=1
            
            if diff != 1:
                found = False
        if found:
            return True
    return False
            
            
