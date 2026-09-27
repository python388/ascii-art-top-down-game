class Armor(object):
  def __init__(self, name, defense, piece, level, cost, itemNum):
    self.name = name
    self.defense = defense
    self.piece = piece
    self.level = level
    self.cost = cost
    self.owned = False
    self.itemNum = itemNum

  def getName(self):
    return self.name
  
  def getItemNum(self):
    return self.itemNum

  def getDefense(self):
    return self.defense

  def getPiece(self):
    return self.piece

  def getCost(self):
    return self.cost

  def getLevel(self):
    return self.level

  def buy(self):
    self.owned = True

  def getOwned(self):
    return self.owned

  def __str__(self):
      return(self.name)