"""
How About A Nice Game Of Chess?
From the 538 riddler
http://fivethirtyeight.com/features/how-about-a-nice-game-of-chess/

First, how long is the longest path a knight can travel on a standard 
8-by-8 board without letting the path intersect itself?

Second, there are unorthodox chess pieces that dont exist in the 
standard game, which are known as fairy chess pieces.  
What are the longest nonintersecting paths that can be taken by the 
camel (which moves like a knight, except 3 squares by 1 square), 
the zebra (3 by 2), and the giraffe (4 by 1)?

"""

# Lets solve this in python recursively

import sys
import pdb

# define the movelist

knightlist = [[-2,-1],[-2,1],[-1,-2],[-1,2],[1,-2],[1,2],[2,-1],[2,1]]

board = [[False, False, False, False, False, False, False, False],
         [False, False, False, False, False, False, False, False],
         [False, False, False, False, False, False, False, False],
         [False, False, False, False, False, False, False, False],
         [False, False, False, False, False, False, False, False],
         [False, False, False, False, False, False, False, False],
         [False, False, False, False, False, False, False, False],
         [False, False, False, False, False, False, False, False]]
      
binaryboard = 0 
testbinaryboard = 2**64 - 1  - (2**24-1)
      
# use a partially filled board for testing, since it finishes much sooner         
testboard = [[False, False, False, False, False, False, False, False],
             [False, False, False, False, False, False, False, False],
             [False, False, False, False, False, False, False, False],
             [True,  True,  True,  True,  True,  True,  True,  True ],
             [True,  True,  True,  True,  True,  True,  True,  True ],
             [True,  True,  True,  True,  True,  True,  True,  True ],             
             [True,  True,  True,  True,  True,  True,  True,  True ],
             [True,  True,  True,  True,  True,  True,  True,  True ]]  
             
# using symmetry, we only need to search 10 starting positions             
startpositions = [[0,0],[0,1],[0,2],[0,3],
                        [1,1],[1,2],[1,3],
                              [2,2],[2,3],
                                    [3,3]]  
                                    
                                    
def searchbinaryboard(board, movelist, movecount, currentx, currenty):                                   
    """
    input to routine are
    the board configurations
    the move count
    currentx and currenty are the current position of the knight
    routine returns the deepest move reached

    """
    highestcount = movecount
    # apply the incoming move
    print movecount
    squarenumber = 8*currenty+currentx
    movedboard = board + 2**squarenumber
    #board[currenty][currentx] = True
    for move in movelist:
        newx = currentx + move[0]
        newy = currenty + move[1]
        if newx < 0 or newy < 0: continue
        if newx > 7 or newy > 7: continue
        squarenumber = 8*newy+newx
        if movedboard & (2**squarenumber) != 0: continue
        # if board[newy][newx]: continue
        newmovecount = searchbinaryboard(movedboard,movelist,movecount+1,newx,newy)
        highestcount = max(highestcount, newmovecount) 
        
    return highestcount
 
 
         
def searchboard(board, movelist, movecount, currentx, currenty):
    """
    input to routine are
    the board configurations
    the move count
    currentx and currenty are the current position of the knight
    routine returns the deepest move reached

    """
    highestcount = movecount
    # apply the incoming move
    print  currentx, currenty, movecount, highestcount
    board[currenty][currentx] = True
    for move in movelist:
        newx = currentx + move[0]
        newy = currenty + move[1]
        if newx < 0 or newy < 0: continue
        if newx > 7 or newy > 7: continue
        if board[newy][newx]: continue
        newmovecount = searchboard(fastcopy(board),movelist,movecount+1,newx,newy)
        highestcount = max(highestcount, newmovecount) 
        
    return highestcount
 
 
def searchstartpositions(board, movelist, startpositions):
    """
    Searches starting from each startposition
    """
    highestcount = 0
    for position in startpositions:
        count = searchboard(fastcopy(board), movelist, 0, position[0], position[1])
        print count
        highestcount = max(highestcount, count)
    return highestcount     
    
def fastcopy(b):
    #pdb.set_trace()
    return     [[b[0][0],b[0][1],b[0][2],b[0][3],b[0][4],b[0][5],b[0][6],b[0][7]],
                    [b[1][0],b[1][1],b[1][2],b[1][3],b[1][4],b[1][5],b[1][6],b[1][7]],
                    [b[2][0],b[2][1],b[2][2],b[2][3],b[2][4],b[2][5],b[2][6],b[2][7]],
                    [b[3][0],b[3][1],b[3][2],b[3][3],b[3][4],b[3][5],b[3][6],b[3][7]],
                    [b[4][0],b[4][1],b[4][2],b[4][3],b[4][4],b[4][5],b[4][6],b[4][7]],
                    [b[5][0],b[5][1],b[5][2],b[5][3],b[5][4],b[5][5],b[5][6],b[5][7]],
                    [b[6][0],b[6][1],b[6][2],b[6][3],b[6][4],b[6][5],b[6][6],b[6][7]],
                    [b[7][0],b[7][1],b[7][2],b[7][3],b[7][4],b[7][5],b[7][6],b[7][7]]]    
    

#print searchstartpositions(board, knightlist, startpositions)
#print searchboard(fastcopy(testboard), knightlist, 0, 0, 0)
#print searchbinaryboard(testbinaryboard, knightlist, 0, 0, 0)
print searchbinaryboard(binaryboard, knightlist, 0, 0, 0)