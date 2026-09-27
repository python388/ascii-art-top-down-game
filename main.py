from random import randint
# Allows generation of random values
import time
# Allows delays
import math
# Allow complex math functions
import ant
# Imports Ant class
import UI
# Improves UI
import hero
# Imports Hero class
import replit
# Imports replit, used for clearing print statements
import string
# Allows aditional string formatting
import armor
# Imports armor class
#smth

newTown = 1
# Makes town intro trigger
xpBoost = False
# Tracks if the Currently equiped armor boosts your xp gain
level = 1
# Tracks witch stage you are on, effecting what the enviornment is
antDrop = 200
# Tracks how much gil enemys drop
levels = ['River Wood']
# Tracks unlocked levels.
hasSword = False
# Tracks if you have gotten a sword
activeLevel = 1
# Tracks witch level you need to beat to progress
money = 10000
# Tracks your available gil
avialableArmor = [
armor.Armor('Leather Bracers', 1, 2, 1, 600, 1),
armor.Armor('Leather Armor', 2, 1, 2, 2000, 2),
armor.Armor('Adventurers Pendent', 0, 3, 3, 4000, 3),
armor.Armor('Defensive Pendent', 2, 3, 4, 10000, 4),
armor.Armor('Studded Leather Bracers', 2, 2, 4, 7000, 5),
armor.Armor('Studded Leather Armor', 3, 1, 4, 10000, 6),
armor.Armor('Iron Shield', 3, 2, 5, 10000, 7)]
# Tracks what armor you can buy at the current village
beenToVillage = False
# Tracks if a village has not been previously visited
antsDefeated = False
# Tracks if you have defeated the ants in the active level
levelChanged = False
# Tracks if the level was changed
name = input('What is your name traveller.')
# Allows the user to make a name for themselves.
town = 'Riverwood'
# Tracks the name of the town you are in
hasDied = False
# Tracks if you have died
def clear():
    replit.clear()
# Creates a function to clear print statements

def townIntro():
    pass
# Contains the intro to the current town

grid = []

def printGrid(listgrid):
# Prints the entire grid
    clear()
    # Clears everything printed
    print(money, 'gil along with', user.getDefense(), 'defense.')
    # Prints the users amount of money, with no new line
    print(user.getHealth(), '/', user.getHealthStart(), 'life')
    # Prints how much health you have, out of your total
    print('You have', user.getXp(), 'Xp. You need', user.getXpLeft(), 'more XP to level up.')
    # Shows how much XP you have, and how much more you need to level up.
    
    yReset = 0
    # Tracks when there is a new line in the grid
    
    gridStr = ''
    # Tracks a string version of the grid to print more efficiently
    
    for value in listgrid:
    # Itterates over every value in the grid, to print all of them
        yReset = yReset + 1
        # Increases the value of the yReset
        
        if yReset < squareLen:
        # SquareLen is the length of each side of the grid. This tests if there should be a new line
            gridStr = gridStr + str(value) + ' '
            # Adds value (the itterated value) to gridStr
        else:
            gridStr = gridStr + str(value) + '\n'
            # Adds a new line, along with value to gridStr
            yReset = 0
            # Resets yReset
    
    print(gridStr)
    # Prints the string version of the grid
    
def move(instance, direction, ant):
# Moves a class instance. Instance, is the class you are moving. Direction is the direction you are moving, ant is a bool, based on if the instance is an ant class.
    grid.pop(convertPair(instance.getX(), instance.getY()))
    grid.insert(convertPair(instance.getX(), instance.getY()), ' ')
    # Replaces the current posstition with a space
    if ant:
    # Tests if an ant is being moved
    
        walls.remove(convertPair(instance.getX(), instance.getY()))
    # Removes an ants current position from walls
    
        if direction == 1:
        # Tests witch direction the ant will move
            if testWall('w', instance) or grid[convertPair(instance.getX(), instance.getY() + 1)] == 'V':
            # Tests if there is a wall in the way
                grid.pop(convertPair(instance.getX(), instance.getY()))
                grid.insert(convertPair(instance.getX(), instance.getY()), 'A') # Inserts an A since an ant is moveing
                walls.append(convertPair(instance.getX(), instance.getY()))
                return False
            else:
                instance.up()
                
        elif direction == 2:
        # The same as above but moving right
            if testWall('d', instance) or grid[convertPair(instance.getX() + 1, instance.getY())] == 'V':
                grid.pop(convertPair(instance.getX(), instance.getY()))
                grid.insert(convertPair(instance.getX(), instance.getY()), 'A') # Inserts an A since an ant is moveing
                walls.append(convertPair(instance.getX(), instance.getY()))
                return False
            else:
                instance.right()
                
        elif direction == 3:
        # The same as above but moving down
            if testWall('s', instance) or grid[convertPair(instance.getX(), instance.getY() - 1)] == 'V':
                grid.pop(convertPair(instance.getX(), instance.getY()))
                grid.insert(convertPair(instance.getX(), instance.getY()), 'A') # Inserts an A since an ant is moveing
                walls.append(convertPair(instance.getX(), instance.getY()))
                return False
            else:
                instance.down()
                
        elif direction == 4:
        # The same as above but moving left
            if testWall('a', instance) or grid[convertPair(instance.getX() - 1, instance.getY())] == 'V':
                grid.pop(convertPair(instance.getX(), instance.getY()))
                grid.insert(convertPair(instance.getX(), instance.getY()), 'A') # Inserts an A since an ant is moveing
                walls.append(convertPair(instance.getX(), instance.getY()))
                return False
            else:
                instance.left()
            
        grid.pop(convertPair(instance.getX(), instance.getY()))
        grid.insert(convertPair(instance.getX(), instance.getY()), 'A') # Inserts an A since an ant is moveing
        walls.append(convertPair(instance.getX(), instance.getY()))
        # Pops the updated postition, and adds an A. Appends the new position to walls
        
    else:
    # This is trigered if the user is moving. It is The same as above, the method names are different, and a U is added instead of an A
    
        if direction == 1:
            # The user moves up
            if testWall('w', instance):
                grid.pop(convertPair(instance.getX(), instance.getY()))
                grid.insert(convertPair(instance.getX(), instance.getY()), 'U')
                return False
            else:
                instance.W()
                
        elif direction == 2:
        # The user moves right
            if testWall('d', instance):
                grid.pop(convertPair(instance.getX(), instance.getY()))
                grid.insert(convertPair(instance.getX(), instance.getY()), 'U')
                return False
            else:
                    instance.D()
                
        elif direction == 3:
        # The user moves down
            if testWall('s', instance):
                grid.pop(convertPair(instance.getX(), instance.getY()))
                grid.insert(convertPair(instance.getX(), instance.getY()), 'U')
                return False
            else:
                instance.S()
            
        elif direction == 4:
        # The user moves left
            if testWall('a', instance):
                grid.pop(convertPair(instance.getX(), instance.getY()))
                grid.insert(convertPair(instance.getX(), instance.getY()), 'U')
                return False
            else:
                instance.A()
        if not(ant) and grid[convertPair(instance.getX(), instance.getY())] == 'V':
        # Checks if the user moved on the Village so as not to delete it
            pass
        else:
            grid.pop(convertPair(instance.getX(), instance.getY()))
            grid.insert(convertPair(instance.getX(), instance.getY()), 'U')
            # The same as above
squareLen = 20
def convertPair(x, y):
    if x < 20 and x >= 0:
        return (squareLen - y) * squareLen + x
    else:
        return 0
    # Converts a cordinate pair to a list index

def doAnt():
# Randomly moves all of the ants
    for index, value in enumerate(ants):
    # Itterates over every ant
        counter = 0
        # Counts to track when to stop reapeting
        
        for i in range(value.getSpeed()):
        # Repeats speed times
            if move(value, randint(1, 4), True):
                pass
                time.sleep(0.5)
            # Calls the move function
            if convertPair(value.getX(), value.getY()) == convertPair(user.getX(), user.getY()):
            # Stops ants from moveing through the user.
                break

ants = []
# An array to track all of the ants.

grid = [
'#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#',
'#', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', '#', '#', '#', '#', ' ', ' ', ' ', ' ', ' ', ' ', '#', 
'#', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', '#', '#', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', 
'#', ' ', '#', '#', ' ', ' ', ' ', '#', '#', '#', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', '#', 
'#', ' ', '#', '#', ' ', ' ', ' ', '#', '#', ' ', ' ', ' ', '#', '#', ' ', '#', '#', '#', '#', '#', 
'#', ' ', ' ', ' ', ' ', '#', ' ', '#', ' ', ' ', ' ', ' ', '#', '#', ' ', '#', '#', '#', ' ', '#', 
'#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#', ' ', '#', 
'#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', 
'#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', 
'#', ' ', ' ', '#', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', '#', 
'#', ' ', ' ', '#', '#', ' ', '#', ' ', ' ', 'V', ' ', '#', '#', '#', ' ', ' ', ' ', ' ', ' ', '#', 
'#', ' ', '#', '#', '#', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', '#', '#', ' ', ' ', ' ', ' ', '#', 
'#', ' ', '#', '#', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', '#', ' ', ' ', ' ', '#', '#', '#', 
'#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', '#', ' ', ' ', ' ', '#', 
'#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', 
'#', ' ', ' ', ' ', ' ', ' ', '#', '#', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#', 
'#', ' ', ' ', ' ', '#', ' ', '#', '#', ' ', ' ', '#', ' ', '#', ' ', ' ', '#', '#', ' ', '#', '#', 
'#', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', 
'#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#', ' ', ' ', '#', '#', '#', ' ', '#', ' ', '#', 
'#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', 
'#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'
]
# The grid

walls = []
# Makes a list to track places you can't move
squareLen = int(math.sqrt(len(grid)))
# Finds the side length of the grid
wallNum = grid.count('#')
# Checks how many walls there are
wallStart = 0
# Sets the start for an index search

for i in range(wallNum):
# Adds all hashtags index value to walls
    walls.append(int(grid.index('#', wallStart)))
    # Adds values to walls
    wallStart = grid.index('#', wallStart) + 1
    # Updates wallStart
    
def onWall(XPos, YPos):
# Checks if a cordinate pair is on a wall
    for i in walls:
        if convertPair(XPos, YPos) == i or grid[convertPair(XPos, YPos)] == 'V':
        # Checks if the position is on a wall, OR the village    
            return True
    return False
    
difficulty = 10
# Controls several ant stats

counter = 0
# Another counter to make a loop that doesn't always progress

while counter < round(difficulty / 2):
# Makes half of difficulty numbrt ants
    X = randint(2, 18)
    Y = randint(2, 18)
    # Takes a random position to test
    if onWall(X, Y):
    # Tests if the value is on a wall
        pass
    else:
        # Creates a ant
        ants.append(ant.Ant(X, Y, math.floor(difficulty / 5), 10, 1, 2))
        counter = counter + 1
        # Changes counter to show that an ant was made

user = hero.Hero(10, 10, 5, 1, 1, 0, 0, 0, 0)
# Makes the main instance of the user class
    
def testWall(direction, thing):
# Tests if there is a wall in a direction
    if direction == 'w':
    # Tests if there is a wall "up"
        for value in walls:
            if convertPair(thing.getX(), thing.getY() + 1) == value:
                # Tests if a IMAGINARY position is on a wall
                return True

    elif direction == 'a':
    # Same as above but testing left
        for index, value in enumerate(walls):
            if convertPair(thing.getX() - 1, thing.getY()) == value:
                return True

    elif direction == 's':
    # Tests down
        for index, value in enumerate(walls):
            if convertPair(thing.getX(), thing.getY() - 1) == value:
                return True

    elif direction == 'd':
    # tests right
        for index, value in enumerate(walls):
            if convertPair(thing.getX() + 1, thing.getY()) == value:
                return True
    else:
        return False
        # False = NOT on wall

grid.pop(convertPair(user.getX(), user.getY()))
grid.insert(convertPair(user.getX(), user.getY()), 'U')
# Adds the user to the grid

for value in ants:
# Defines the ants, and adds them to grid and wall
    grid.pop(convertPair(value.getX(), value.getY()))
    grid.insert(convertPair(value.getX(), value.getY()), 'A')
    walls.append(convertPair(value.getX(), value.getY()))

printGrid(grid)
# Prints the grid
print('\n Hello',name, 'you have traveled to the town of River Wood to help the people combat the giant ants. You need to get a sword. Perhaps you should go to River Wood to find one. To move press W, A, S, or D, and then press enter.')
input('')
# Adds a small tutorial

while not(hasDied):
# Makes the loop that the game takes place in.
    printGrid(grid)
    # Prints the grid
    
    if hasSword:
        turn = input('Move with W, A, S, D, and attack with WW, AA, SS, DD')
    else:
        turn = input('Move with W, A, S, D')
        
    # Takes input for what the player wants to do
    if turn == 'w':
    # Moves the user in a direction based on their input.
        move(user, 1, False)
    elif turn == 'a':
        move(user, 4, False)
    elif turn == 's':
        move(user, 3, False)
    elif turn == 'd':
        move(user, 2, False)
    elif turn == 'ww':
        if hasSword:
            hapticGrid = list(grid)
        # Checks if you have a sword before allowing you to attack
            for value in ants:
            # Itterates over ants to see if you hit them
                for i in range(user.getRange()):
                # Repeats times equal to your attack range
                    change = i + 1
                    # Sets the change from the users positon to find which squares you hit
                    if convertPair(value.getX(), value.getY()) == convertPair(user.getX(), user.getY() + change):
                    # Checks if you hit an ant
                        for i in range(user.getStrength()):
                        # Does damage depending on your damage
                            if value.takeDamage():
                            # Causes the ant to take damage. Returns true if the ant dies
                                grid.pop(convertPair(value.getX(), value.getY()))
                                grid.insert(convertPair(value.getX(), value.getY()), 'X')
                                printGrid(grid)
                                # Adds an X to the grid where you killed an ant
                                time.sleep(0.3)
                                # Sleeps so that you can see the X
                                grid.pop(convertPair(value.getX(), value.getY()))
                                grid.insert(convertPair(value.getX(), value.getY()), ' ')
                                # Updates the grid to not contain the ant
                                walls.remove(convertPair(value.getX(), value.getY()))
                                ants.remove(value)
                                # Removes the ants from walls and ants
                                money = money + antDrop
                                # Increases your money
                                if xpBoost:
                                # If you have a boost to your xp
                                    user.gainXp(xpBoost)
                                    # Gain extra xp
                                    
                                if user.gainXp(value.getXpDrop()):
                                # Gives you XP
                                    printGrid(grid)
                                    # Prints the grid in case there was level up text
                                break
            for i in range(user.getRange()):
                change = i + 1
                if user.getY() + change <= 20 and user.getY() + change >= 0:
                    if not(hapticGrid[convertPair(user.getX(), user.getY() + change)] == 'X'):
                        hapticGrid.pop(convertPair(user.getX(), user.getY() + change))
                        hapticGrid.insert(convertPair(user.getX(), user.getY() + change), '|')
            printGrid(hapticGrid)
            time.sleep(0.3)
            printGrid(grid)
    
    elif turn == 'aa':
    # Veiw above
        if hasSword:
            hapticGrid = list(grid)
            for value in ants:
                for i in range(user.getRange()):
                    change = i + 1
                    if convertPair(value.getX(), value.getY()) == convertPair(user.getX() - change, user.getY()):
                        for i in range(user.getStrength()):
                            if value.takeDamage():
                                hapticGrid.pop(convertPair(value.getX(), value.getY()))
                                hapticGrid.insert(convertPair(value.getX(), value.getY()), 'X')
                                grid.pop(convertPair(value.getX(), value.getY()))
                                grid.insert(convertPair(value.getX(), value.getY()), ' ')
                                walls.remove(convertPair(value.getX(), value.getY()))
                                ants.remove(value)
                                money = money + value.getHealth() * 100
                                if xpBoost:
                                    user.gainXp(xpBoost)
                                    
                                if user.gainXp(value.getXpDrop()):
                                    printGrid(grid)
                                break
            for i in range(user.getRange()):
                change = i + 1
                if user.getX() - change <= 20 and user.getX() - change >= 0:
                    if not(hapticGrid[convertPair(user.getX() - change, user.getY())] == 'X'):
                        hapticGrid.pop(convertPair(user.getX() - change, user.getY()))
                        hapticGrid.insert(convertPair(user.getX() - change, user.getY()), '—')
            printGrid(hapticGrid)
            time.sleep(0.3)
            printGrid(grid)
                    
    elif turn == 'ss':
    # Veiw above
        if hasSword:
            hapticGrid = list(grid)
            for value in ants:
                for i in range(user.getRange()):
                    change = i + 1
                    if convertPair(value.getX(), value.getY()) == convertPair(user.getX(), user.getY() - change):
                        for i in range(user.getStrength()):
                            if value.takeDamage():
                                grid.pop(convertPair(value.getX(), value.getY()))
                                grid.insert(convertPair(value.getX(), value.getY()), 'X')
                                printGrid(grid)
                                time.sleep(0.3)
                                grid.pop(convertPair(value.getX(), value.getY()))
                                grid.insert(convertPair(value.getX(), value.getY()), ' ')
                                walls.remove(convertPair(value.getX(), value.getY()))
                                ants.remove(value)
                                money = money + value.getHealth() * 100
                                if xpBoost:
                                    user.gainXp(xpBoost)
                                    
                                if user.gainXp(value.getXpDrop()):
                                    printGrid(grid)
                                break
            for i in range(user.getRange()):
                change = i + 1
                if convertPair(user.getX(), user.getY() - change) <= 400 and convertPair(user.getX(), user.getY() - change) >= 0:
                    if not(hapticGrid[convertPair(user.getX(), user.getY() - change)] == 'X'):
                        hapticGrid.pop(convertPair(user.getX(), user.getY() - change))
                        hapticGrid.insert(convertPair(user.getX(), user.getY() - change), '|')
            printGrid(hapticGrid)
            time.sleep(0.3)
            printGrid(grid)
                            
    elif turn == 'dd':
    # Veiw above
        if hasSword:
            hapticGrid = list(grid)
            for value in ants:
                for i in range(user.getRange()):
                    change = i + 1
                    if convertPair(value.getX(), value.getY()) == convertPair(user.getX() + change, user.getY()):
                        for i in range(user.getStrength()):
                            if value.takeDamage():
                                grid.pop(convertPair(value.getX(), value.getY()))
                                grid.insert(convertPair(value.getX(), value.getY()), 'X')
                                printGrid(grid)
                                time.sleep(0.3)
                                grid.pop(convertPair(value.getX(), value.getY()))
                                grid.insert(convertPair(value.getX(), value.getY()), ' ')
                                walls.remove(convertPair(value.getX(), value.getY()))
                                ants.remove(value)
                                money = money + value.getHealth() * 100
                                if xpBoost:
                                    user.gainXp(xpBoost)
                                    
                                if user.gainXp(value.getXpDrop()):
                                    printGrid(grid)
                                break
            for i in range(user.getRange()):
                change = i + 1
                if not(hapticGrid[convertPair(user.getX() + change, user.getY())] == 'X'):
                    hapticGrid.pop(convertPair(user.getX() + change, user.getY()))
                    hapticGrid.insert(convertPair(user.getX() + change, user.getY()), '—')
            printGrid(hapticGrid)
            time.sleep(0.3)
            printGrid(grid)
                            
    elif turn == 'DEV TOOLS':
    # Allows the DEV TOOLS cheat code
        for value in ants:
        # Itterates damage over each ant
            for i in range(5):
            # Does five damage to each ant
                if value.takeDamage():
                # Does damage
                    grid.pop(convertPair(value.getX(), value.getY()))
                    grid.insert(convertPair(value.getX(), value.getY()), ' ')
                    walls.remove(convertPair(value.getX(), value.getY()))
                    ants.remove(value)
                    money = money + value.getHealth() * 100
                if user.gainXp(value.getXpDrop()):
                    printGrid(grid)
                break
                # Does the attack and level up system listed above
    elif turn == 'e':
        print('you own')

        options = []
        for value in avialableArmor:
            if value.getOwned():
                options.append(value.getName() + ' which has ' + str(value.getDefense()) + " defense.")
            
        choice = UI.dropDownNumber('What do you want to equip?', 'nothing', *options)

        if choice == 0:
            pass
        else:
            for value in avialableArmor:
                if value.getOwned() and value.getItemNum() == choice:
                    user.updateArmor(value.getPiece(), value.getDefense())
                    UI.display('You equiped ' + value.getName())
                
                    if value.getItemNum() == 3:
                        xpBoost = 50

    if grid[convertPair(user.getX(), user.getY())] == 'V':
    # Tests if you are at the village
        levelChanged = True
        # Makes it so the outside world will reset
        for value in ants:
        # Kills all the ants
            ants.remove(value)
            # Removes a value from ants
            value.die()
            # Calls the die method for ants
            
        while True:
        # While you are in the village
            clear()
            # Clears everything
                
            if not(beenToVillage):
            # If you haven't seen the town intro
                turn = UI.dropDown('Hello, ' + name + ' welcome to our town of ' + town + ' here we are in dire need of adventurers to clear the area of giant ants. Will you help us?', 'yes', 'no')
                # Gives you a quest
                if    turn == 'yes':
                # Checks if you accept
                    if not(hasSword):
                    # Checks if you have gotten the sword which you get in the first town
                        UI.display('Thank you so much. As a token of our appreciation, take this sword. \n \nTo use it press w, a, s, or d TWICE, and then hit enter.\n')
                        # Teaches you how to attack
                        hasSword = True
                        # Lets the game know that you have a sword
                        beenToVillage = True
                        # Marks that you have been to the village
                        newTown = 0
                    else:
                    # If you allready have the sword
                        townIntro()
                        # Calls the town intro
                else:
                    # If you said no to the quest
                    UI.display('Please come back if you change your mind.')
                    # Asks you to come back if you change your mind
                    break
                    # Stops the village loop
                
            turn = UI.dropDown('Where do you want to go in the village?', 'inn', 'blacksmith', 'the stables', 'leave')
            # Gives you your turn options
                
            clear()
            # Clears any intro text
                
            if turn == 'leave':
            # If you want to leave
                break
                # Breaks the village loop
                
            elif turn == 'inn':
            # If you want to rest at the inn
                turn = UI.dropDown('Rest at the inn to re-fill your health for 100 gil, You have ' + str(money) + ' gil.', 'yes', 'no')
                # Asks you if you want to pay the cost
                if turn    == 'yes' and money >= 100:
                # If you can pay
                    money = money - 100
                    # Makes you pay
                    user.heal()                        
                    # Heals you
                elif turn == 'yes' and money < 100:
                # If you can't afford the inn
                    UI.display("I'm sorry, but you don't have enough gil.")
                    # Tells you that you don't have enough gil
                    
                elif turn == 'no':
                # If you miss clicked
                    UI.display('Please come back later.')
                    # Asks you to come back later
                        
            elif turn == 'blacksmith':
            # If you go to the blacksmiths
                inBlacksmith = True
                
                while inBlacksmith:
                    options = []
                    for value in avialableArmor:
                    # Itterates over existing armor
                        if value.getLevel() <= level:
                        # Checks if you are progressed enough to buy said armor
                            if value.getName() == 'Adventurers Pendent':
                            # Checks if you want to buy the special equipment
                                options.append("Adventurers Pendent's, for" + str(value.getCost()) + "gil. It gives you extra XP.")
                                # Tells you what adventurers pendents do
                            else: 
                            # For normal armor
                                options.append(value.getName() + ' for ' + str(value.getCost()) + ' gil. It gives you ' + str(value.getDefense()) + " defense.")
                                # Prints armor stats
                            
                    choice = UI.dropDownNumber('Hello ' + name + ' what do you want to buy?' + ' You have ' + str(money) + ' gil', 'leave', *options)
                        
                    # Asks what you want to buy
                        
                    for value in avialableArmor:
                    # Itterates over all armor
                        if value.getItemNum() == choice and money >= value.getCost():
                        # Tests if the current Itterated value is what you want and if you can afford it
                            value.buy()
                            # Calls the    buy method
                            money -= value.getCost()
                            # Spends money
                            UI.display('you bought ' + value.getName())
                            # Tells you that you bought something
                        elif value.getItemNum() == choice and money < value.getCost():
                            UI.display('You cannot afford that')

                        elif choice == 0:
                            inBlacksmith = False

            elif turn == 'the stables':
            # If you choose to go to the stables
                clear()
                # Clears previous prints

                options = []
                for index, value in enumerate(levels):
                # For each level
                    options.append(value)
                    print(value)
                    # Prints unlocked towns, and a number to type to go to them
                turn = UI.dropDownNumber('\n Hello, where do you wish to go.', 'leave', *options)
                if not(turn == 0):
                    # Asks which town you want to go too.
                    if True:
                    # Checks that an integer was givin as input
                        if turn <= activeLevel:
                        # Checks that a level is unlocked
                            level = int(turn)
                        
                            levelChanged = True
                            break
                    else:
                        input('Please type a number')
                    
    grid.pop(convertPair(user.getX(), user.getY()))
    grid.insert(convertPair(user.getX(), user.getY()), 'U')
        
    if level == 1 and levelChanged:
        grid = [
'#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#',
'#', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', '#', '#', '#', '#', ' ', ' ', ' ', ' ', ' ', ' ', '#', 
'#', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', '#', '#', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', 
'#', ' ', '#', '#', ' ', ' ', ' ', '#', '#', '#', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', '#', 
'#', ' ', '#', '#', ' ', ' ', ' ', '#', '#', ' ', ' ', ' ', '#', '#', ' ', '#', '#', '#', '#', '#', 
'#', ' ', ' ', ' ', ' ', '#', ' ', '#', ' ', ' ', ' ', ' ', '#', '#', ' ', '#', '#', '#', ' ', '#', 
'#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#', ' ', '#', 
'#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', 
'#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', 
'#', ' ', ' ', '#', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', '#', 
'#', ' ', ' ', '#', '#', ' ', '#', ' ', ' ', 'V', ' ', '#', '#', '#', ' ', ' ', ' ', ' ', ' ', '#', 
'#', ' ', '#', '#', '#', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', '#', '#', ' ', ' ', ' ', ' ', '#', 
'#', ' ', '#', '#', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', '#', ' ', ' ', ' ', '#', '#', '#', 
'#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', '#', ' ', ' ', ' ', '#', 
'#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', 
'#', ' ', ' ', ' ', ' ', ' ', '#', '#', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#', 
'#', ' ', ' ', ' ', '#', ' ', '#', '#', ' ', ' ', '#', ' ', '#', ' ', ' ', '#', '#', ' ', '#', '#', 
'#', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', 
'#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#', ' ', ' ', '#', '#', '#', ' ', '#', ' ', '#', 
'#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', 
'#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#']
        
        for value in ants:
            ants.remove(value)
            value.die()
                
        counter = 0
        
        antDrop = 200
            
        difficulty = 10
            
        user.defX(10)
        user.defY(10)
        grid.pop(convertPair(user.getX(), user.getY()))
        grid.insert(convertPair(user.getX(), user.getY()), 'U')
        
        levelChanged = False    

        town = 'River Wood'
        
        walls = []
        squareLen = int(math.sqrt(len(grid)))
        wallNum = grid.count('#')
        wallStart = 0

        for i in range(wallNum):
            walls.append(int(grid.index('#', wallStart)))
            wallStart = grid.index('#', wallStart) + 1
        while counter < round(difficulty / 2):
            X = randint(2, 18)
            Y = randint(2, 18)
            if onWall(X, Y) or convertPair(X, Y) == grid.index('V') or convertPair(X, Y) == convertPair(10, 10):
                pass
            else:
                ants.append(ant.Ant(X, Y, math.floor(difficulty / 5), 10, 1, 2))
                counter = counter + 1
                
        for value in ants:
            grid.pop(convertPair(value.getX(), value.getY()))
            grid.insert(convertPair(value.getX(), value.getY()), 'A')
            walls.append(convertPair(value.getX(), value.getY()))
        if newTown == 1:
            beenToVillage = False
            newTown = 2
    
    if level == 2 and levelChanged:
        grid = [
'#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#',
'#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', 
'#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', 
'#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', 
'#', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#', ' ', ' ', '#', ' ', ' ', ' ', '#', 
'#', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', 
'#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', 
'#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', 
'#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', 
'#', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', 
'#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'V', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', 
'#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', '#', ' ', ' ', ' ', '#', 
'#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', 
'#', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', 
'#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', 
'#', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', 
'#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', '#', 
'#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', 
'#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', 
'#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'
]
        
        for value in ants:
            ants.remove(value)
            value.die()
                
        counter = 0
        
        antDrop = 400
            
        difficulty = 25
            
        user.defX(10)
        user.defY(10)
        grid.pop(convertPair(user.getX(), user.getY()))
        grid.insert(convertPair(user.getX(), user.getY()), 'U')
        
        levelChanged = False    

        town = 'Waystone'
        
        walls = []
        squareLen = int(math.sqrt(len(grid)))
        wallNum = grid.count('#')
        wallStart = 0

        for i in range(wallNum):
            walls.append(int(grid.index('#', wallStart)))
            wallStart = grid.index('#', wallStart) + 1
        while counter < round(difficulty / 2):
            X = randint(2, 18)
            Y = randint(2, 18)
            if onWall(X, Y) or convertPair(X, Y) == grid.index('V') or convertPair(X, Y) == convertPair(10, 10):
                pass
            else:
                ants.append(ant.Ant(X, Y, math.floor(difficulty / 5), 20, 1, 5))
                counter = counter + 1
                
        for value in ants:
            grid.pop(convertPair(value.getX(), value.getY()))
            grid.insert(convertPair(value.getX(), value.getY()), 'A')
            walls.append(convertPair(value.getX(), value.getY()))
            
        if newTown == 2:
            beenToVillage = False
            newTown = 3
    
    if level == 3 and levelChanged:
        grid = [
'#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#',
'#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', '#', '#', '#', '#', '#', 
'#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', ' ', '#', '#', '#', '#', ' ', '#', '#', '#', 
'#', ' ', ' ', '#', '#', ' ', ' ', ' ', '#', '#', '#', ' ', '#', '#', '#', '#', ' ', '#', '#', '#', 
'#', '#', ' ', '#', '#', ' ', ' ', ' ', '#', '#', '#', ' ', '#', '#', '#', '#', ' ', '#', '#', '#', 
'#', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', '#', ' ', '#', '#', '#', 
'#', '#', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', ' ', '#', '#', '#', 
'#', '#', '#', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#', ' ', '#', '#', '#', 
'#', '#', '#', '#', '#', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#', ' ', '#', '#', '#', 
'#', '#', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', '#', '#', 
'#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'V', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', 
'#', ' ', ' ', '#', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', ' ', ' ', '#', '#', 
'#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', ' ', ' ', '#', '#', 
'#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#', ' ', ' ', ' ', '#', '#', '#', ' ', ' ', ' ', '#', 
'#', '#', '#', ' ', '#', '#', ' ', ' ', '#', '#', ' ', ' ', ' ', ' ', '#', '#', ' ', ' ', ' ', '#', 
'#', '#', '#', ' ', '#', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', 
'#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#', '#', 
'#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#', 
'#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', 
'#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'
]
        
        for value in ants:
            ants.remove(value)
            value.die()
                
        counter = 0
        
        antDrop = 600
            
        difficulty = 75
            
        user.defX(10)
        user.defY(10)
        grid.pop(convertPair(user.getX(), user.getY()))
        grid.insert(convertPair(user.getX(), user.getY()), 'U')
        
        levelChanged = False    

        town = 'Evergreen'
        
        walls = []
        squareLen = int(math.sqrt(len(grid)))
        wallNum = grid.count('#')
        wallStart = 0

        for i in range(wallNum):
            walls.append(int(grid.index('#', wallStart)))
            wallStart = grid.index('#', wallStart) + 1
        while counter < 20:
            X = randint(2, 18)
            Y = randint(2, 18)
            if onWall(X, Y) or convertPair(X, Y) == grid.index('V') or convertPair(X, Y) == convertPair(10, 10):
                pass
            else:
                ants.append(ant.Ant(X, Y, math.floor(difficulty / 5), 100, 2, 10))
                counter = counter + 1
                
        for value in ants:
            grid.pop(convertPair(value.getX(), value.getY()))
            grid.insert(convertPair(value.getX(), value.getY()), 'A')
            walls.append(convertPair(value.getX(), value.getY()))
        
        if newTown == 3:
            beenToVillage = False
            newTown = 4
    
    if level == 4 and levelChanged:
        grid = [
'#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#',
'#', '#', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', '#', 
'#', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#', 
'#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', 
'#', ' ', '#', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#', ' ', '#', '#', 
'#', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', 
'#', ' ', '#', ' ', ' ', ' ', '#', ' ', '#', ' ', '#', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#', 
'#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', 
'#', '#', ' ', '#', ' ', '#', ' ', '#', ' ', ' ', ' ', ' ', '#', ' ', '#', ' ', ' ', ' ', ' ', '#', 
'#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#', ' ', ' ', '#', 
'#', ' ', '#', ' ', ' ', ' ', '#', ' ', '#', 'V', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', 
'#', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#', 
'#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#', '#', '#', 
'#', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#', 
'#', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', 
'#', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#', 
'#', ' ', ' ', '#', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', '#', '#', ' ', '#', '#', 
'#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', 
'#', ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', '#', ' ', '#', ' ', '#', '#', '#', ' ', '#', ' ', '#', 
'#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', 
'#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#']
        
        for value in ants:
            ants.remove(value)
            value.die()
                
        counter = 0
        
        antDrop = 900
            
        difficulty = 125
            
        user.defX(10)
        user.defY(10)
        grid.pop(convertPair(user.getX(), user.getY()))
        grid.insert(convertPair(user.getX(), user.getY()), 'U')
        
        levelChanged = False

        town = 'Herdaz'
        
        walls = []
        squareLen = int(math.sqrt(len(grid)))
        wallNum = grid.count('#')
        wallStart = 0

        for i in range(wallNum):
            walls.append(int(grid.index('#', wallStart)))
            wallStart = grid.index('#', wallStart) + 1
        while counter < round(15):
            X = randint(2, 18)
            Y = randint(2, 18)
            if onWall(X, Y) or convertPair(X, Y) == grid.index('V') or convertPair(X, Y) == convertPair(10, 10):
                pass
            else:
                ants.append(ant.Ant(X, Y, math.floor(difficulty / 5), 200, 2, 20))
                counter = counter + 1
                
        for value in ants:
            grid.pop(convertPair(value.getX(), value.getY()))
            grid.insert(convertPair(value.getX(), value.getY()), 'A')
            walls.append(convertPair(value.getX(), value.getY()))
        if newTown == 4:
            beenToVillage = False
            newTown = 5
    
    if not(ants) and level == activeLevel:
        activeLevel += 1
        if activeLevel == 2:
            levels.append('waystone')
            newTown = 2
            def townIntro():
                global newTown
                global town
                global beenToVillage
                if level == 2:
                    print('Thank you for agreeing to help us. We will be sure to supply you with the best food available.\n \n YOU GAIN MORE LIFE')
                    for i in range(10):
                        user.heartContainer()
                    input()
                    newTown = 0
                    beenToVillage = True
                    # Marks that you have been to the village
        if activeLevel == 3:
            levels.append('Evergreen')
            newTown = 3
            def townIntro():
                global newTown
                global town
                global beenToVillage
                if level == 3:
                    print('Thank you for agreeing to help us. Make use of our encampment of soldiers to learn more sword fighting techniques. \n \n YOU GAIN 500 XP')
                    for i in range (10):
                        user.heartContainer()
                    input('')
                    newTown = 0
                    beenToVillage = True
                # Marks that you have been to the village
        if activeLevel == 4:
            levels.append('Herdaz')
            newTown = 4
            def townIntro():
                global newTown
                global town
                global beenToVillage
                global money
                if level == 4:
                    print('Thank you for agreeing to help us. please make use of this money at the black smith. \n\n YOU GAIN 5000 GIL.')
                    money += 5000
                    input('')
                    newTown = 0
                    beenToVillage = True
                
    doAnt()
    
    for value in ants:
        if convertPair(user.getX(), user.getY()) == convertPair(value.getX(), value.getY()):
            for i in range(value.getDamage() - user.getDefense()):
                if user.takeDamage():
                    input('you got eaten by a giant ant. Best of luck next time.')
                    printGrid(grid)
                    hasDied = True
                
            printGrid(grid)
            time.sleep(0.5)
                    
            if value.getAttackReturn() == 1:
                walls.remove(convertPair(value.getX(), value.getY()))
                grid.pop(convertPair(value.getX(), value.getY()))
                grid.insert(convertPair(value.getX(), value.getY()), 'U')

                value.up()
                    
                grid.pop(convertPair(value.getX(), value.getY()))
                walls.append(convertPair(value.getX(), value.getY()))
                grid.insert(convertPair(value.getX(), value.getY()), 'A')
        
            elif value.getAttackReturn() == 2:
                walls.remove(convertPair(value.getX(), value.getY()))
                grid.pop(convertPair(value.getX(), value.getY()))
                grid.insert(convertPair(value.getX(), value.getY()), 'U')
            
                value.right()
                    
                grid.pop(convertPair(value.getX(), value.getY()))
                walls.append(convertPair(value.getX(), value.getY()))
                grid.insert(convertPair(value.getX(), value.getY()), 'A')
            
            elif value.getAttackReturn() == 3:
                walls.remove(convertPair(value.getX(), value.getY()))
                grid.pop(convertPair(value.getX(), value.getY()))
                grid.insert(convertPair(value.getX(), value.getY()), 'U')
                    
                value.down()
                    
                grid.pop(convertPair(value.getX(), value.getY()))
                walls.append(convertPair(value.getX(), value.getY()))
                grid.insert(convertPair(value.getX(), value.getY()), 'A')
            
            elif value.getAttackReturn() == 4:
                walls.remove(convertPair(value.getX(), value.getY()))
                grid.pop(convertPair(value.getX(), value.getY()))
                grid.insert(convertPair(value.getX(), value.getY()), 'U')
                    
                value.left()
                
                grid.pop(convertPair(value.getX(), value.getY()))
                walls.append(convertPair(value.getX(), value.getY()))
                grid.insert(convertPair(value.getX(), value.getY()), 'A')