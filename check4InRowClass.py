from typing import TypedDict
from vars import *


class ChekedStateResult(TypedDict):
    isValid:bool
    error:str

class fourInRow():
    def __init__(self, position, params, size):
        self.params = params
        self.position = position
        self.size = size
        self.menu = {
            "1" : self.displayField,
            "2" : self.displayParams,
            "3" : self.checkState
            # 4 : sys.exit()
        }

    def displayField(self):
        print("Position \n")
        for i in range(self.size[1], 0, -1):
            curRow = []
            for j in range(self.size[0]):
                curRow.append(self.position[j][i - 1])
            print(' '.join(curRow))
    
    def displayParams(self):
        print(f'Number of moves: {self.params["numberOfMoves"]}')
        print(f'Last move was made by : {self.params["lastMove"]}')
        print(f'First move was made by : {self.params["firstMove"]}')

    def printMenu(self):
        for key in MENU.keys():
            print(f'{key} : {MENU[key]}')
    
    def positionCli(self):
        while True:
            self.printMenu()
            choice = input("Your choice ...:  ")
            if choice in self.menu.keys():
                print(choice)
                self.menu[choice]()
                continue
            else:
                print("Invalid value")
                continue            
    
    def checkState(self) -> ChekedStateResult:
        check_state_result = {}
        return check_state_result
    

    # Cheks that there is no flying chips
    def checkGravity(self) -> bool:
        is_valid = True
        return is_valid
    

    # Checks that amounts of Y and R are equal or differs 
    # no more that by 1
    def checkEqualAmount(self) -> bool:
        is_valid = True
        return is_valid

    # Checks whether there was a win before
    def wasWin(self) ->bool:
        is_valid = True
        return is_valid
    