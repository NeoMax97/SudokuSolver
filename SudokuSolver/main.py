from itertools import filterfalse


class Sudoku(object):

    # Initialize variables
    def __init__(self):
        self.setUpBoard()

    # Returns an empty Sudoku Board
    def setUpBoard(self):
        res = dict()
        for x in self.getAllPos(self):
            res.update(dict([(x, list(range(1, 10)))]))
        return res

    # Returns a list of all positions of a Sudoku Board
    def getAllPos(self):
        allPos = list()
        i = 0
        while (i < 81):
            allPos.append((i // 9, i % 9))
            i = i + 1
        return allPos

    # Parse a string into a Board
    def parse(self, string):
        return self.parseHelper(self, zip(list(string), self.getAllPos(self)))

    # Helper Function for parse()
    def parseHelper(self, list):
        board = Board(self.setUpBoard(self))
        for elem in list:
            val = elem[0]
            key = elem[1]
            if val == '.':
                continue
            else:
                board = board.place(key[0], key[1], int(val))
        return board

    # Calculates peers of a given position.
    # According to the rules, these 'peers' cannot hold the same value.
    def calcPeers(self, row, col):
        rowPeers = list(map(lambda r: (r, col), list(range(0, 9))))  # Vertical Peers
        colPeers = list(map(lambda c: (row, c), list(range(0, 9))))  # Horizontal Peers
        boxRow = (row//3)*3
        boxCol = (col//3)*3
        boxRowList = list()
        boxRowList.append(boxRow)
        boxRowList.append(boxRow+1)
        boxRowList.append(boxRow+2)
        boxColList = list()
        boxColList.append(boxCol)
        boxColList.append(boxCol+1)
        boxColList.append(boxCol+2)
        boxPeers = []
        boxPeers = list(map(lambda r: list(map(lambda c: (r, c), boxColList)), boxRowList))  # Peers in the same 3x3 box
        allPeers = rowPeers+colPeers+list(self.flatten(boxPeers))
        result = filterfalse((lambda tuple: tuple[0] == row and tuple[1] == col), allPeers)
        return self.removeDup(result)

    # Helper Function : Flattens a list of lists into a single list
    def flatten(*iterables):
        for iter in iterables:
            for it in iter:
                for elem in it:
                    yield elem

    # Helper Function : Removes duplicates while preserving order
    def removeDup(iterable):
        seen = list()
        for x in iterable:
            if not (x in seen):
                seen.append(x)
        return seen

    def peers(self, row, col):
        return self.calcPeers(self, row, col)


# available is a dict where key = (row, col) and value = list(possibles)
class Board(object):

    import Sudoku

    # Initialize variables
    def __init__(self, available):
        self.avail = available

    # Return list of available values at position of Board
    def availableValuesAt(self, row, col):
        return self.avail.get((row, col), list(range(0, 10)))

    # Return the assigned value at position. If not assigned, return 0
    def valueAt(self, row, col):
        result = self.avail[(row, col)]
        if type(result) == int:
            return result
        else:
            return 0

    # Check if the Board is solved
    def isSolved(self):
        for x in Sudoku.getAllPos(self):
            if type(self.avail[x]) == int:
                continue
            else:
                return False
        return True

    # Check if the Board is unsolvable
    def isUnsolvable(self):
        for x in Sudoku.getAllPos(self):
            if self.avail[x] == list():
                return True
        return False

    # Places a value and calls removeValue to remove values from peers
    def place(self, row, col, value):
        board = self.deep_copy(self.avail)
        newBoard = self.removeValue(Sudoku.peers(Sudoku, row, col), value, board)
        newBoard.update(dict([((row, col), value)]))
        return Board(newBoard)

    # Removes a value from all peers of a given positions
    def removeValue(self, peers, value, board):
        for peer in peers:
            vals = board[peer]
            if type(vals) == int:
                continue
            if value in vals:
                board[peer] = list(filter(lambda x: x != value, board[peer]))
                if (len(board[peer]) == 1):    # If we reduce a position to one value, place that value
                    newBoard = Board(board).place(peer[0], peer[1], board[peer][0]).avail
                    board = newBoard
        return board

    # Helper Function: Deep copy
    def deep_copy(self, board):  # takes a dict() as parameter
        newBoard = dict()
        for key in Sudoku.getAllPos(self):
            newBoard.update(dict([(key, board[key])]))
        return newBoard

    # Returns a list of Boards, each representing a move made
    def nextStates(self):
        res = list()
        if self.isUnsolvable():
            return res
        elif self.isSolved():
            res.append(Board(self.avail))
            return res
        else:
            res = self.getStates(self.avail)
            return res

    # Helper Function for nextStates
    def getStates(self, board):
        nextList = list()
        keys = Sudoku.getAllPos(self)
        for key in keys:
            currList = list()
            vals = board[key]  # list of possible values
            if type(vals) == int:
                continue
            else:
                for val in vals:
                    newBoard = Board(self.deep_copy(board))
                    currList.append(newBoard.place(key[0], key[1], val))
                nextList.extend(currList)
        return nextList

    # Solve the Board
    def solve(self):
        if self.isSolved():
            return Board(self.avail)
        elif self.isUnsolvable():
            return None
        else:
            return self.runSolve(self.nextStates())

    # Helper Function for solve()
    def runSolve(self, list):
        for board in list:
            if board.isSolved():
                return board
            elif board.isUnsolvable():
                continue
            else:
                # print("neither")
                tail = list[list.index(board)+1:]
                solved = self.runSolve(tail)
                if solved is not None:
                    return solved
                else:
                    return self.runSolve(board.nextStates())
        return None
