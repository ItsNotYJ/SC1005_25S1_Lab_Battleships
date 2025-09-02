# Global Variables
player1 = "Computer"
player2 = "User"

layer = 2
width, height = 10

valid, hit, miss = False

ship1 = {
    name: "Submarine",
    orientation: "v",
    coordinates: [],
    health: 3
}

ship2 = {
    name: "Carrier",
    orientation: "v",
    coordinates: [],
    health: 4
}

# List of Messages
welmes = "Welcome to Battleships! Hit ENTER to continue"
setupMessages = [
    "Please enter your preferred orientation of your ship i.e, 'v' -> Vertical / 'h' -> Horizontal: ",
    f"These are your available ships to place: \n1.{ship1}\n2.{ship2}\nPlease select an option (1 / 2): ",
]

'''
Please enter coordinate of the attack center point in following this format (row,col,depth). E.g.
A,4,1
Note: depth = 0 represents the subsea layer, and depth = 1 represents the surface level.
Enter coordinates: B,3,0
Hit at area centering B,3,0
'''

# Functions for the game
def isInputValid():
    pass

# Main loop and Games States
main = True
isSetupDone = False
startGame = False

while main:
    input(welmes)
    if isSetupDone == False:
        player2 = input("Please")
        v = input(setupMessages[0])
        