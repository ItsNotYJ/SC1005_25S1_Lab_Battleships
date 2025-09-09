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
    if shipLength == 4 and ori == validOrientations[0] :
    
    elif shipLength == 4 and ori == validOrientations[1]:         
            
    else: # If ship is submarine
        
            
#TODO: Add validation for already added ships on the board
def isPlacementCoordValid(shipLength, width, height, ori):
    if 0 < width <= 10 and 0 < height <= 10:
        # Check if ship placed exceeds boundaries #1 = vertical, #2 = horizontal
        if ori in validOrientations:
            if ori == validOrientations[0] and (height - 1) + shipLength <= 9: # Vertical 0 to 9 (1 - 10)
                return True

            elif ori == validOrientations[1] and (width - 1) + shipLength <= 9: # Horizontal 0 to 9 (1 - 10)
                return True

    else:
        print("Your coordinate has exceeded the board boundaries of width - 10 and height - 10. Please try again.")
        
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
            chosenShip = input(setupMessages[2])
            
            # If user chooses 1, start setup for submarine
            if chosenShip == "1":
                print(f"\nLet's setup submarine no.{submarineCount + 1}\n")
                if submarineCount != 3:
                    pass
                else:
                    print("Your have already placed all 3 of your submarines. Please setup your carriers if you have not done so.")
            else: # If user chooses 2, start setup for carrier
                pass
            
        
        