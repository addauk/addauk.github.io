def solution(matrix):
    
    r = len(matrix)
    c = len(matrix[0])
    
    print(r)
    print(c)
    cost = 0
    ghostCol = []
            
    for i in range(r):
        
        for j in range(c):
            if j not in ghostCol: 
                if matrix[i][j] != 0:
                    cost += matrix[i][j]
                else:
                    ghostCol.append(j)
    
    return cost 
                
                
        
        
                