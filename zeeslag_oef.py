from random import randrange

matrix_bord = [[False, False, False, False], [False, False, False, False], [False, False, False, False]]

def spawnCheck(matrix, row, col):

    # check if already exists
    if (matrix[row][col]):
        return False

    # check sides
    collideTop = False
    collideBottom = False
    collideLeft = False
    collideRight = False
    if (row != 0 and matrix[row-1][col]): # check Top
        collideTop = True
    if (row != len(matrix)-1 and matrix[row+1][col]): # check Bottom
        collideBottom = True
    if (col != 0 and matrix[row][col-1]): # check Left
        collideLeft = True
    if (col != len(matrix[0])-1 and matrix[row][col+1]): # check Right
        collideRight = True
   
    # return true if nothing colided 
    if(collideTop == collideBottom == collideLeft == collideRight):
        return True
    else:
        return False

def spawnBooten():
    aantalBooten = 0
    while (aantalBooten != 3):
        pos = randrange(12)
        col = pos % 4
        row = pos // 4
        if (spawnCheck(matrix_bord, row, col)):
            print(str(col) + ", " + str(row))
            aantalBooten += 1;
            matrix_bord[row][col] = True
        else:
            print(str(col) + " - " + str(row))
        
    

spawnBooten()    
