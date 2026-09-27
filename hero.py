import replit
def clear():
    replit.clear()

class Hero(object):
    def __init__(self, x, y, health, strength, Range, xp, armor, bracers, accesories):
        self.x = x
        self.y = y
        self.health = health
        self.healthStart = health
        self.strength = strength
        self.range = Range
        self.xp = xp
        self.xpLeft = 20
        self.rangeTracker = 3
        self.rangeTrackerStart = self.rangeTracker
        self.xpStart = self.xpLeft
        self.armor = armor
        self.bracers = bracers
        self.accesories = accesories
        self.healthIncrease = 2
        self.defense = armor + bracers + accesories
    
    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getHealth(self):
        return self.health

    def getHealthStart(self):
        return self.healthStart

    def getDefense(self):
        return self.defense

    def getStrength(self):
        return self.strength

    def getRange(self):
        return self.range

    def getXp(self):
        return self.xp

    def updateArmor(self, piece, defense):
        if piece == 1:
            self.armor = defense
        elif piece == 2:
            self.bracers = defense
        else:
            self.accesories = defense
      
        self.defense = self.armor + self.bracers + self.accesories

    def getXpLeft(self):
        return self.xpLeft

    def D(self):
        self.x = self.x + 1

    def S(self):
        self.y = self.y - 1

    def A(self):
        self.x = self.x - 1

    def W(self):
        self.y = self.y + 1

    def takeDamage(self):
        self.health = self.health - 1
    
        if self.health == 0:
            return True
            del self

    def heal(self):
        self.health = self.healthStart

    def heartContainer(self):
        self.healthStart += 1
        self.heal()

    def defX(self, X):
        self.x = X

    def defY(self, Y):
        self.y = Y

    def levelUp(self):
        clear()
        print('YOU LEVELED UP!!!')
        self.strength += 1
        print('Your strength increased. You now do', self.strength, 'damage on a hit.\n')
        self.healthStart += self.healthIncrease
        self.healthIncrease +=2
        self.heal()
        print('Your overall health increased.\n')
        self.rangeTracker -= 1
        if self.rangeTracker == 0:
            self.range += 1
            print('Your attack range has increased. Your attacks now reach ants', self.range, 'squares away.')
            self.rangeTrackerStart += 3
            self.rangeTracker = self.rangeTrackerStart
        self.xpStart = round(self.xpStart * 2.25)
        self.xpLeft = self.xpStart
        if input('') == 'yay':
            print("I'm glad your happy. Why don't you get some more health, and strength, and even some more range")
            self.healthStart += self.healthIncrease
            self.healthIncrease +=2
            self.heal()
            self.range += 1
            self.strength += 1
            input('')
      
    def gainXp(self, amount):
        self.xp += amount
        self.xpLeft -= amount
        if self.xpLeft <= 0:
            self.levelUp()
            return True
  
    def defStrength(self, amount):
        self.strength = amount

    def defRange(self, amount):
        self.range = amount