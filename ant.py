from random import randint

class Ant(object):
  def __init__(self, x, y, health, xpDrop, speed, damage, image='A'):
    self.x = x
    self.y = y
    self.startHealth = health
    self.health = health
    self.attackReturn = 0
    self.xpDrop = xpDrop
    self.speed = speed
    self.damage = damage
    self.image = image
  
  def __str__(self):
    return str(self.x)

  def getX(self):
    return self.x

  def getY(self):
    return self.y

  def getXpDrop(self):
    return self.xpDrop

  def getDamage(self):
    return self.damage

  def getSpeed(self):
    return self.speed

  def up(self):
    self.y = self.y + 1
    self.attackReturn = 3

  def right(self):
    self.x = self.x + 1
    self.attackReturn = 4

  def down(self):
    self.y = self.y - 1
    self.attackReturn = 1

  def left(self):
    self.x = self.x - 1
    self.attackReturn = 2

  def getHealth(self):
    return self.startHealth

  def getAttackReturn(self):
    return self.attackReturn
  
  def changeReturn(self, update):
    self.attackReturn = update

  def takeDamage(self):
    self.health = self.health - 1
    
    if self.health <= 0:
      return True
      del self

  def die(self):
    del self