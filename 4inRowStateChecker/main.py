from typing import TypedDict
from check4InRowClass import fourInRow
from vars import *

class GameParams(TypedDict):
    numberOfMoves:int
    firstMove:str
    lastMove:str

# function to input int >= 0
def inputInt( name) -> int:
        while True:
            try:
                par = int(input(f'Input {name}: '))
                if par < 0:
                    continue
            except ValueError:
                print("That's not an int!") 
                continue
            else:
                break
        return par


# function to input only allow values that are sent in possble values
def inputPossibleValue(text, possibleValues):
    while True:
        val = input(text + '\n')
        if val in possibleValues:
                break
        else:
            print("Invalid value")
            continue    
    return val


# Input of a column
def inputColumn( height, columnNum) -> list():
    curColumn = []
    for cellRow in range(height):
        text = f'''Input value of cell in column: {columnNum + 1},
                            row {cellRow + 1} starting from bottom,
                            possble values: R, Y, A'''
        curPoint = inputPossibleValue(text, POSSIBLE_VALUES)
        if curPoint == "A":
            curPoint = None
        curColumn.append(curPoint)
    return curColumn


# Input of the game parametrs
def inputParams() -> GameParams:
    textFirstMove = f'''Input who was first to put chip,
                possble values: R, Y'''
    textLastMove = f'''Input who was last to put chip,
                            possble values: R, Y'''
    params = {}
    numberOfMoves = inputInt("Number of moves")
    firstMove = inputPossibleValue(textFirstMove, PLAYERS_COLORS)
    lastMove = inputPossibleValue(textLastMove, PLAYERS_COLORS)
    params = {'numberOfMoves': numberOfMoves, 
              "firstMove": firstMove, 
              "lastMove":lastMove}
    return params


# Input of a size
def inputSize() -> tuple:
    print("Input width and height")
    while True:
        width = inputInt("width")
        if width >= 4:
            break
        else:
            print("At least 4")
            continue
    while True:
        height = inputInt("height")
        if height >= 4:
            break
        else:
            print("At least 4")
            continue
    size = (width, height)
    return size 


# Input of a field
def inputField(size) -> list:
    position = list()
    for columnNum in range(size[0]):
        curColumn = inputColumn(size[1], columnNum)
        position.append(curColumn)
    return position

# Input of the whole state
def startInput():
    size = inputSize()
    position = inputField(size)
    params = inputParams()
    return position, params, size


def main():
    position , params, size = startInput()
    gameState = fourInRow(position, params, size)
    gameState.positionCli()

if __name__ == "__main__":
    main()
    