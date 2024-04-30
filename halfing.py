import character

class Halfing(character.Character):
  """Concrete class for Halfing
  Attributes: 
    name - string name of the halfing
  Funcitons: 
    abilities - list of abilities [0, 0, 0, 1]
    constitution - int of constitution
    strength - int of strength
    wisdom - int of wisdom"""
  def __init__(self, name):
    super().__init__(name + " the Halfing")

  def abilities(self):
    return [0, 0, 0, 1]  # Archery, Fighting, Fire, Healing

  def constitution(self):
    return 15

  def strength(self):
    return 10

  def wisdom(self):
    return 13