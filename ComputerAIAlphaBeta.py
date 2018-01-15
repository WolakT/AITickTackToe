from Grid import Grid
from random import randint
import collections
import math


class ComputerAI:
    def __init__(self):
        self.counter = 0
        self.play = 0
    def makeMove(self, grid):
        self.counter = 0
        # moves = grid.getAvailableMoves()
        # move = randint(0, len(moves) - 1)
        # if self.play == 0:
        #     self.play += 1
        #     return 4
        # else:

        result = self.minimise(grid, -math.inf, math.inf)[0]
        return result
    # def decision(self, grid):


    def maximise(self, grid, alpha, beta):
        if self.isTerminalState(grid):
            value = self.evaluate(grid)
            return None, value
        maxMove = None
        maxVal = -math.inf
        moves = grid.getAvailableMoves()
        # print(moves)
        for move in moves:
            copyGrid = grid.clone()
            copyGrid.makeMove(move, "X")
            result = self.minimise(copyGrid, alpha, beta)
            if result[1] >= maxVal:
                maxVal = result[1]
                maxMove = move
                optimalGrid = copyGrid.clone()
            if maxVal >= beta:
                print(f"the biggest grid till now is  {optimalGrid.printGrid()}")
                print(f"beta equals {beta}")
                return maxMove, maxVal
            if maxVal > alpha:
                alpha = maxVal
        return maxMove, maxVal

    def minimise(self, grid, alpha, beta):
        if self.isTerminalState(grid):
            value = self.evaluate(grid)
            return None, value
        minMove = None
        minVal = math.inf
        moves = grid.getAvailableMoves()
        for move in moves:
            copyGrid = grid.clone()
            copyGrid.makeMove(move, "O")
            result = self.maximise(copyGrid, alpha, beta)
            if result[1] <= minVal:
                minVal = result[1]
                minMove = move
                optimalGrid = copyGrid.clone()
            if minVal <= alpha:

                print(f"the biggest grid till now is  {optimalGrid.printGrid()}")
                print(f"alpha equals {alpha}")

                return minMove, minVal
            if minVal < beta:
                beta = minVal
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
        if grid.gridMap[4] == "X":
            points += 1
        #if grid.gridMap[4] == "O":
          #  points -= 1
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
