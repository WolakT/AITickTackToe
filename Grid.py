

class Grid(object):
	def __init__(self):
		self.gridMap = {x: "." for x in range(9) }

	def printGrid(self):
		for i in range(len(self.gridMap)):
				if (i +1) % 3   == 0:
					print(self.gridMap[i], end= "\n")
				else:
					print(self.gridMap[i], end= " ")
			
	def getAvailableMoves(self):
		moves = list()
		for i in range(len(self.gridMap)):
			if self.gridMap[i] == ".":
				moves.append(i)
		return moves

	def makeMove(self, move, sign):
		if self.gridMap[move] == ".":
			self.gridMap[move] = sign
			return True
		else:
			return False

	def isOver(self):
		if len(self.getAvailableMoves()) == 0:
			return True
		elif self.checkHorizontally():
			print("horizontally")
			return True
		elif self.checkVertically():
			print("vertically")
			return True
		else:
			return False

	def checkHorizontally(self):
		for i in (0,3,6):
			firstRow = set()
			for j in range(3):
				first = self.gridMap[i+j]
				firstRow.add(first)
				print(f"lenght of the set is: {len(firstRow)}")
				print("row contains: " , firstRow)
			if len(firstRow) == 1 and first != ".":
				return True
		return False

	def checkVertically(self):
		for i in (0,1,2):
			firstColumn = set()
			for j in (0,3,6):
				first = self.gridMap[i+j]
				firstColumn.add(first)
				print(f"lenght of the set is: {len(firstColumn)}")
				print("column contains: " , firstColumn)
			if len(firstColumn) == 1 and first != ".":
				return True
		return False
		