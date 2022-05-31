def solution(image):

    #for every row over 3, calc an extra set of columns
    rows = len(image)
    maxr = rows - 2
    cols = len(image[0])
    maxc = cols -2
    results = []
    for i in range(maxr):
        
    #for every column over 3, calc an extra box
        boxes = []
        for j in range(maxc):
            block = 0
            for x in range(3):
                row = 0
                for y in range(3):
                    row += image[x+i][y+j]
                block += row
            #build box values
            boxes.append(math.floor(block/9))
        
        #append box values
        results.append(boxes)
    
    return results

    
    
