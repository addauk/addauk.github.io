def solution(bishop, pawn):
    new = bishop
    #UR Move
    while new[0] <= 'h' and new[1] <= '8':
        if new == pawn:
            return True
        
        new = chr(ord(new[0])+1) + chr(ord(new[1])+1)

        
    new = bishop    
    #DR Move
    while new[0] <= 'h' and new[1] > '0':
    
        if new == pawn:
            return True
        
        new = chr(ord(new[0])+1) + chr(ord(new[1])-1)
    new = bishop
    #UL Move
    while new[0] >= 'a' and new[1] <= '8':
    
        if new == pawn:
            return True
        
        new = chr(ord(new[0])-1) + chr(ord(new[1])+1)
    new = bishop   
    #DL Move
    while new[0] >= 'a' and new[1] > '0':
    
        if new == pawn:
            return True
        
        new = chr(ord(new[0])-1) + chr(ord(new[1])-1)
    return False
