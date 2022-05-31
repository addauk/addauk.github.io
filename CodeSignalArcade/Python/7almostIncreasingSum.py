def solution(sequence):

    for i in range(len(sequence)-1):
        
        if sequence[i] >= sequence[i + 1]:
            #we've hit a problem index
            #lets check the list without the current OR the next index to see if they pass as if either of them do then we have found an element we can remove
            if increasingSequence(sequence[:i] + sequence[i+1:]) or \
                    increasingSequence(sequence[:i+1] + sequence[i+2:]):
                return True
            else:
                
                return False
    return True


def increasingSequence(sequence):
    for i in range(len(sequence) - 1):
        if sequence[i] >= sequence[i + 1]:
            return False
    return True         
                
