from typing import TypedDict
from vars import *
import numpy as np
import math


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
            print(' '.join(str(item) for item in curRow))
    
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
    

    def countChips(self) -> dict:
        numRed = 0
        numYellow  = 0
        for column in self.position:
            numRed += column.count("R")
            numYellow += column.count("Y")
        return {
            "RED":numRed,
            "YELLOW":numYellow
        }
    

    # Aggregate state checkings
    def checkState(self) -> ChekedStateResult:
        print(f'Gravity check.... {self.checkGravity()}')
        print(f'Equal (or +-1) amount of chips... {self.checkEqualAmount()}')
        print(f'Moves order check.... {self.checkMovesOrder()}')
        print(f'Right amount of moves check...{self.checkRightAmountOfMoves()}')
        # self.wasWin()
        check_state_result = {}
        return check_state_result
    

    # Cheks that there is no flying chips
    def checkGravity(self) -> bool:
        for column  in self.position:
            if (column.index(None) < column.index("R") or
            column.index(None) < column.index("Y")):
                return False
        return True
    

    # Checks that amounts of Y and R are equal or differs 
    # no more that by 1
    def checkEqualAmount(self) -> bool:
        amount = self.countChips()
        return abs(amount["RED"] - amount["YELLOW"]) <= 1
    

    # Checks moves order
    def checkMovesOrder(self) -> bool:
        amount = self.countChips()
        if  amount["RED"] == amount["YELLOW"]:
            return True
        else:
            if ((amount["RED"] - amount["YELLOW"] == 1 and 
                self.params["firstMove"] == "R") or 
                (amount["YELLOW"] - amount["RED"] == 1 and 
                self.params["firstMove"] == "Y")):
                    return True
            else:
                return False


    def checkRightAmountOfMoves(self) -> bool:
        amount = self.countChips()
        total = amount["RED"] + amount["YELLOW"]
        return math.ceil(total / 2) == self.params["numberOfMoves"]
   
    # Checks whether there was a win before
    def wasWin(self) ->bool:
        field = np.array(self.position)
        # print(field)
        # print((field[:,:-2:] == field[:,1:-1:]) & (field[:,:-2:] == field[:,2::]))
        # print((field[:-2:,:] == field[1:-1:,:]) & (field[:-2:,:] == field[2::,:]))
        # print((field[:-2:,:-2:] == field[1:-1:,1:-1:]) & (field[:-2:,:-2:] == field[2::,2::]))
        is_valid = True
        return is_valid
    