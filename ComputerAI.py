from Grid import Grid
from random import randint
import math


class ComputerAI:
    def makeMove(self, grid):
        print('test')
        moves = grid.getAvailableMoves()
        move = randint(0, len(moves) - 1)
        return self.maximise(grid)[0]

    # def decision(self, grid):


    def maximise(self, grid):
        if self.isTerminalState(grid):
            value = self.evaluate(grid)
            return None, value
        maxMove = None
        maxVal = -math.inf
        moves = grid.getAvailableMoves()
        print(moves)
        for move in moves:
            copyGrid = grid.clone()
            copyGrid.makeMove(move, "O")
            result = self.minimise(copyGrid)
            if result[1] > maxVal:
                maxVal = result[1]
                maxMove = result[0]
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
            copyGrid.makeMove(move, "X")
            result = self.maximise(copyGrid)
            if result[1] < minVal:
                minVal = result[1]
                minMove = result[0]
        return minMove, minVal

    def evaluate(self, grid):
        points = 0
        if grid.checkHorizontally():
            points += 1
        if grid.checkVertically():
            points += 1
        if grid.checkDiagonally():
            points += 1
        return points

    def isTerminalState(self, grid):
        if len(grid.getAvailableMoves()) == 0:
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
