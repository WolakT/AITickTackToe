from Grid import Grid
from random import randint
import math


class ComputerAI:

    def __init__(self):
       self.counter = 0
       self.play = 0

    def makeMove(self, grid):
        self.counter = 0
        #moves = grid.getAvailableMoves()
        #move = randint(0, len(moves) - 1)
        if self.play == 0:
            self.play += 1
            return 4
        else:
            return self.minimise(grid)[0]

    # def decision(self, grid):


    def maximise(self, grid):
        if self.isTerminalState(grid):
            value = self.evaluate(grid)
            return None, value
        maxMove = None
        maxVal = -math.inf
        moves = grid.getAvailableMoves()
        #print(moves)
        for move in moves:
            copyGrid = grid.clone()
            copyGrid.makeMove(move, "X")
            result = self.minimise(copyGrid)
            if result[1] >= maxVal:
                maxVal = result[1]
                maxMove = move
        return maxMove, maxVal

    def minimise(self, grid):
        if self.isTerminalState(grid):
            value = self.evaluate(grid)
            return None, value
        minMove = None
        minVal = math.inf
        moves = grid.getAvailableMoves()
        for move in moves:
            copyGrid = grid.clone()
            copyGrid.makeMove(move, "O")
            result = self.maximise(copyGrid)
            if result[1] <= minVal:
                minVal = result[1]
                minMove = move
        return minMove, minVal

    def evaluate(self, grid):
        points = 0
        
        if grid.checkHorizontally() and grid.lastMove == "O":
            points -= 1
        if grid.checkHorizontally() and grid.lastMove == "X":
            points += 1
        if grid.checkVertically() and grid.lastMove == "O":
            points -= 1
        if grid.checkVertically() and grid.lastMove == "X":
            points += 1
        if grid.checkDiagonally() and grid.lastMove == "O":
            points -= 1
        if grid.checkDiagonally() and grid.lastMove == "X":
            points += 1
        return points

    def isTerminalState(self, grid):
        if grid.isOver() or grid.isWin():
            print(f"terminal state reached with following grid {grid.printGrid()}")
            print(f"following is the state value: {self.evaluate(grid)}")
            self.counter += 1
            print(f"followin is the couner value: {self.counter}")
            return True
        else:
            return False


# def run():
#     comp = ComputerAI()
#     grid = Grid()
#     move = comp.makeMove(grid)
#     grid.makeMove(move, "X")
#     grid.printGrid()
#
#
# run()
