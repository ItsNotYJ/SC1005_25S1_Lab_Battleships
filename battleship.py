# Global Variables
player1 = "Computer"
player2 = "User"

valid, hit, miss = False, False, False
# 1 -> Vertical, 2 -> Horizontal
validOrientations = ["1", "2"]

ship1 = {
    "name": "Submarine",
    "coordinates": [],
    "length": 3
}

ship2 = {
    "name": "Carrier",
    "coordinates": [],
    "length": 4
}

shipList = [ship1, ship2]

# List of Messages
welmes = "Welcome to Battleships! Hit ENTER to continue"
setupMessages = [
    "Please enter your name: ", #0
    "Please choose your preferred orientation of your ship: \n1. Vertical\n2. Horizontal\n\nEnter your selection: ", #1
    f"Please select a ship to setup: \n1.{ship1["name"]} {ship1["length"]} units\n2.{ship2["name"]} {ship2["length"]} units\n\n\
Please select an option (1 / 2), you have a total of 3 carriers and 3 submarines available for placement: ", #2
]

'''
Please enter coordinate of the attack center point in following this format (row,col,depth). E.g.
A,4,1
Note: depth = 0 represents the subsea layer, and depth = 1 represents the surface level.
Enter coordinates: B,3,0
Hit at area centering B,3,0
'''

# Functions for the game
def initBoard():
    pass

def displayBoard():
    pass

def setupBoard():
    pass

def isInputValid(userInput):
    if userInput != "":
        return True
    return False

def isOrientationValid(ori):
    if ori.lower() in validOrientations:
        return True
    return False

def generateShipOnBoard(shipLength, width, height, ori):
    tempCoor = []
    shipLength = int(shipLength)
    width = int(width)
    height = int(height)
    
    if shipLength == 4: # If ship is carrier
        if ori == validOrientations[0]:
            for x in range(0, shipLength): # Horizontal
                if x == 0:
                    tempCoor.append([width, height])
                else:
                    tempCoor.append([width + x, height])
            ship2["coordinates"].append(tempCoor)
            print(ship2["coordinates"])
        else:
            for y in range(0, shipLength): # Vertical
                if y == 0:
                    tempCoor.append([width, height])
                else:
                    tempCoor.append([width, height + y])
            ship2["coordinates"].append(tempCoor)
            print(ship2["coordinates"])
    
    elif shipLength == 3: # If ship is submarine
        if ori == validOrientations[0]: 
            for x in range(0, shipLength): # Horizontal
                if x == 0:
                    tempCoor.append([width, height])
                else:
                    tempCoor.append([width + x, height])
            ship1["coordinates"].append(tempCoor)
            print(ship1["coordinates"])
        else:
            for y in range(0, shipLength): # Vertical
                if y == 0:
                    tempCoor.append([width, height])
                else:
                    tempCoor.append([width, height + y])
            ship1["coordinates"].append(tempCoor)
            print(ship1["coordinates"])
            
def isPlacementCoordValid(shipLength, width, height, ori):
    tempCoor = []
    
    if 1 <= width <= 10 and 1 <= height <= 10:
        # Check if ship placed exceeds boundaries #1 = vertical, #2 = horizontal
        if ori in validOrientations:
            if ori == validOrientations[0] and (height - 1) + shipLength <= 10: # Vertical (1 - 10)
                for x in range(0, shipLength): # Horizontal
                    if x == 0:
                        tempCoor.append([width, height])
                    else:
                        tempCoor.append([width + x, height])
                    
                # Check if coordinates already exist, to prevent overlapping ships from being placed
                if shipLength == 3:
                    for ship in ship1["coordinates"]:
                        for coor in ship:
                            for inputCoor in tempCoor:
                                if inputCoor == coor:
                                    print("There are ships already placed on these coordinates. Please select another coordinate.")
                                    return False
                else:
                    for ship in ship2["coordinates"]:
                        for coor in ship:
                            for inputCoor in tempCoor:
                                if inputCoor == coor:
                                    print("There are ships already placed on these coordinates. Please select another coordinate.")
                                    return False

                return True
            elif ori == validOrientations[1] and (width - 1) + shipLength <= 10: # Horizontal (1 - 10)
                for y in range(0, shipLength): # Vertical
                    if y == 0:
                        tempCoor.append([width, height])
                    else:
                        tempCoor.append([width, height + y])
                
                # Check if coordinates already exist, to prevent overlapping ships from being placed
                if shipLength == 3:
                    for ship in ship1["coordinates"]:
                        for coor in ship:
                            for inputCoor in tempCoor:
                                if inputCoor == coor:
                                    print("There are ships already placed on these coordinates. Please select another coordinate.")
                                    return False
                else:
                    for ship in ship2["coordinates"]:
                        for coor in ship:
                            for inputCoor in tempCoor:
                                if inputCoor == coor:
                                    print("There are ships already placed on these coordinates. Please select another coordinate.")
                                    return False
                
                return True
            else:
                print("The ship will exceed the board boundaries of width - 10 and height - 10. Please try again\n")
                return False
        else:
            print("Invalid orientation, please select a valid orientation\n")
            return False
    else:
        print("Your coordinate has exceeded the board boundaries of width - 10 and height - 10. Please try again.\n")
        
    return False

# Main loop and Games States
main = True
isSetupDone = False
startGame = False

# Setup states
submarineCount = 0
carrierCount = 0
nameChosen = False
isShipPlaced = False

while main:
    input(welmes)
    print()
    print("Let's setup your game!")
    
    # If setup is not done isSetupDone = False
    while isSetupDone != True:
        if not nameChosen:
            player2 = input(setupMessages[0])
            
            # Check if input is valid
            if not isInputValid(player2):
                print("\nPlease enter a valid name!\n")
                continue
            else:
                print(f"\nHi {player2} let's setup your board now!\n")
                nameChosen = True # Set name to chosen
        
        if not isShipPlaced:
            if submarineCount == 3 and carrierCount == 3:
                isShipPlaced = True
            else:
                isShipPlaced = False
            
            chosenShip = input(setupMessages[2])
            
            # If user chooses 1, start setup for submarine
            if chosenShip not in ["1", "2"]:
                print("\nInvalid selection, please select a ship to setup!\n")
                continue
            elif chosenShip == "1": #Submarine
                if submarineCount != 3:
                    print(f"\nLet's setup submarine no.{submarineCount + 1}\n")
                    
                    ori = input(setupMessages[1])
                    xCoor = input("Please choose a value 1 - 10 to place your ship along the horizontal axis: ")
                    yCoor = input("Please choose a value 1 - 10 to place your ship along the vertical axis: ")
                    
                    if isInputValid(xCoor) and isInputValid(yCoor) and not isPlacementCoordValid(3, int(xCoor), int(yCoor), ori):
                        continue
                    else:
                        generateShipOnBoard(3, xCoor, yCoor, ori)
                        submarineCount += 1
                        continue
                else:
                    print("Your have already placed all 3 of your submarines. Please setup your carriers if you have not done so.")
            elif chosenShip == "2": #Carrier
                print(f"\nLet's setup carrier no.{carrierCount + 1}\n")
                if carrierCount != 3:
                    pass
                else:
                    print("Your have already placed all 3 of your carriers. Please setup your submarines if you have not done so.")
            else: # If user chooses 2, start setup for carrier
                pass
    
            