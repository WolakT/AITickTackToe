
import Grid

def main():
	testGrid = Grid.Grid()
	testGrid.printGrid()
	print(testGrid.getAvailableMoves())
	print(testGrid.makeMove(4, "X"))
	testGrid.printGrid()
	print(testGrid.makeMove(1, "X"))
	print(testGrid.makeMove(7, "X"))
	print(testGrid.makeMove(2, "X"))
	print(testGrid.makeMove(5, "X"))
	#print(testGrid.makeMove(0, "O"))
	print(testGrid.makeMove(3, "O"))
	print(testGrid.makeMove(6, "O"))
	testGrid.printGrid()
	print(testGrid.getAvailableMoves())
	print(testGrid.isOver())
	print(testGrid.checkVertically())
main()