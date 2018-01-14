import Grid
import ComputerAI
import ComputerAIAlphaBeta


class GameManagerAdversarial(object):
    def __init__(self):
        self.grid = Grid.Grid()
        if False:
            self.computer = ComputerAI.ComputerAI()
        else:
            self.computer = ComputerAIAlphaBeta.ComputerAI()

    def main(self):
        while not self.grid.isOver() and not self.grid.isWin():
            # computer plays

            self.grid.makeMove(self.computer.makeMove(self.grid), "O")
            print(self.grid.lastMove)
            if self.grid.isOver() or self.grid.isWin():
                break
            self.grid.isWin()
            # human player
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
            if self.grid.isWin():
                player = self.grid.lastMove
                print(f"Player {player} won!")
        self.grid.printGrid()

    def validateInput(self, sign, field):
        strMessage = ""
        if sign != "X" and sign != "O":
            strMessage = "Invalid sign"
        elif field < 0 or field > 8:
            strMessage = "Invalid field index"
        return strMessage


def run():
    manager = GameManagerAdversarial()
    manager.main()


run()
