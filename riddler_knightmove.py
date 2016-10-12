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
         
def searchboard(board, movelist, movecount, currentx, currenty):
    """
    input to routine is the board configurations and the move count
    routine returns the deepest move reached
    currentx and currenty are the current position of the knight
    """
    highestcount = movecount
    #for move in movelist:
        

    return highestcount
    
def fastcopy(self, b):
    return     [[b[0][0],b[0][1],b[0][2],b[0][3],b[0][4],b[0][5],b[0][6],b[0][7]],
                    [b[1][0],b[1][1],b[1][2],b[1][3],b[1][4],b[1][5],b[1][6],b[1][7]],
                    [b[2][0],b[2][1],b[2][2],b[2][3],b[2][4],b[2][5],b[2][6],b[2][7]],
                    [b[3][0],b[3][1],b[3][2],b[3][3],b[3][4],b[3][5],b[3][6],b[3][7]],
                    [b[4][0],b[4][1],b[4][2],b[4][3],b[4][4],b[4][5],b[4][6],b[4][7]],
                    [b[5][0],b[5][1],b[5][2],b[5][3],b[5][4],b[5][5],b[5][6],b[5][7]],
                    [b[6][0],b[6][1],b[6][2],b[6][3],b[6][4],b[6][5],b[6][6],b[6][7]],
                    [b[7][0],b[7][1],b[7][2],b[7][3],b[7][4],b[7][5],b[7][6],b[7][7]]]    
    

print searchboard(board, knightlist, 0, 0, 0)