def solution(matrix):
    rows, cols = len(matrix),len(matrix[0])
    print(rows,cols)
    mines = [([0]*cols) for i in range(rows)]
    for i in range(rows):
          
        for j in range(cols):
                
            if matrix[i][j]:
                for y in range(j-1,j+2):
                    for x in range(i-1,i+2):
                        if not (x == i and y == j):
                            if x >= 0 and y >= 0: 
                                if x < rows and y < cols:
                                    mines[x][y] +=1
      
        


    return mines