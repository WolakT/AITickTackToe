from Grid import Grid
from random import randint
class ComputerAI:
	
	def makeMove(self, grid):
		print('test')
		moves = grid.getAvailableMoves()
		move = randint(0,len(moves)-1)
		return moves[move]
def main():
	comp = ComputerAI()
	grid = Grid()
	move = comp.makeMove(grid)
	grid.makeMove(move, "X")
	grid.printGrid()

main()
