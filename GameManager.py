import Grid

class GameManager(object):
	def __init__(self):
		self.grid = Grid.Grid()
	def main(self):
		while not self.grid.isOver():
			self.grid.printGrid()
			userMove = input("> ")
			sign = userMove[1]
			field = int(userMove[0])
			flag = self.grid.makeMove(field,sign)
			while not flag:
				print("this move is wrong type again:")
				userMove = input("> ")
				sign = userMove[1]
				field = int(userMove[0])
				flag = self.grid.makeMove(field,sign)
			

def run():
	manager = GameManager()
	manager.main()
run()