
"""
https://leetcode.com/problems/valid-tic-tac-toe-state/description/
A Tic-Tac-Toe board is given as a string array board. Return True if and only if it is possible to reach this board position during the course of a valid tic-tac-toe game.

The board is a 3 x 3 array, and consists of characters " ", "X", and "O".  The " " character represents an empty square.

Here are the rules of Tic-Tac-Toe:

Players take turns placing characters into empty squares (" ").
The first player always places "X" characters, while the second player always places "O" characters.
"X" and "O" characters are always placed into empty squares, never filled ones.
The game ends when there are 3 of the same (non-empty) character filling any row, column, or diagonal.
The game also ends if all squares are non-empty.
No more moves can be played if the game is over.
Example 1:
Input: board = ["O  ", "   ", "   "]
Output: false
Explanation: The first player always plays "X".

Example 2:
Input: board = ["XOX", " X ", "   "]
Output: false
Explanation: Players take turns making moves.

Example 3:
Input: board = ["XXX", "   ", "OOO"]
Output: false

Example 4:
Input: board = ["XOX", "O O", "XOX"]
Output: true
Note:

"""
class Solution(object):
    def validTicTacToe(self, board):
        """
        :type board: List[str]
        :rtype: bool
        """
        if board == ["   ","   ","   "]:
            return True
        joinl = "".join(board)
        a = joinl.count("X") - joinl.count("O")
        prev = False
        if a == 1:     
            for i in range(9):
                if joinl[i] =="X":
                    temp  = joinl[:i]+ " " +joinl[i+1:]
                    if not self.isSomeOneWin([temp[0:3], temp[3:6], temp[6:10]  ]):
                        prev = True 
            return prev
        elif a == 0:
            
            for i in range(9):
                if joinl[i] =="O":
                    temp = joinl[:i]+ " " + joinl[i+1:]
                    print not self.isSomeOneWin([temp[0:3], temp[3:6], temp[6:10]  ])
                    if not self.isSomeOneWin([temp[0:3], temp[3:6], temp[6:10]  ]):
                        prev = True 
            return prev
        else:
            return False
    def isSomeOneWin(self,board):
        
        for i in board:
            if i in ['XXX', 'OOO']:
                return True
        for i in range(3):
            if board[0][i] +board[1][i] +board[2][i] in ['XXX', 'OOO']:
                return True
        if board[0][0] +board[1][1] +board[2][2] in ['XXX', 'OOO']:
                return True
        if board[0][2] +board[1][1] +board[2][0] in ['XXX', 'OOO']:
                return True
        return False