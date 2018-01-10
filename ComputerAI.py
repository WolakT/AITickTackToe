from Grid import Grid
from random import randint
import math


class ComputerAI:
    def makeMove(self, grid):

        moves = grid.getAvailableMoves()
        move = randint(0, len(moves) - 1)
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
        grid.printGrid()
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
        if grid.isOver():
            print(f"terminal state reached with following grid {grid.printGrid()}")
            print(f"following is the state value: {self.evaluate(grid)}")
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
