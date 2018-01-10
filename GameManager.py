import Grid


class GameManager(object):
    def __init__(self):
        self.grid = Grid.Grid()

    def main(self):
        while not self.grid.isOver():
            while True:
                self.grid.printGrid()
                userMove = input("> ")
                sign = userMove[1]
                field = int(userMove[0])
                validation = self.validateInput(sign, field)
                if validation == "":
                    if self.grid.makeMove(field, sign):
                        break
                    else:
                        print("Move already done")
                else:
                    print(validation)
        self.grid.printGrid()

    def validateInput(self, sign, field):
        strMessage = ""
        if sign != "X" and sign != "O":
            strMessage = "Invalid sign"
        elif field < 0 or field > 8:
            strMessage = "Invalid field index"
        return strMessage


def main():
    manager = GameManager()
    manager.main()


main()
