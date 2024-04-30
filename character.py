import abc

class Character(abc.ABC):
  """ Abstract class for a character.
  Attributes: 
  name (str) = name of the character
  Functions: 
  abilities() - returns a list of the character's abilities
  constitution() - returns the character's constitution
  strength() - returns the character's strength
  wisdome() - returns the character's wisdom"""
  def __init__(self, n):
    self.name = n

  def __str__(self):
    abilities_format = ""
    ability = self.abilities()
    if ability[0] > 0:
      abilities_format += "\nArchery: Level " + str(ability[0])
    if ability[1] > 0:
      abilities_format += "\nFighting: Level " + str(ability[1])
    if ability[2] > 0:
      abilities_format += "\nFire Magic: Level " + str(ability[2])
    if ability[3] > 0:
      abilities_format += "\nHealing: Level " + str(ability[3])
    return f"{self.name}\n-Abilities- {abilities_format}\n-Stats- \nCon: {self.constitution()}\nStr: {self.strength()}\nWis: {self.wisdom()}"

  @abc.abstractmethod
  def abilities(self):
    pass

  @abc.abstractmethod
  def constitution(self):
    pass

  @abc.abstractmethod
  def strength(self):
    pass
    
  @abc.abstractmethod
  def wisdom(self):
    pass