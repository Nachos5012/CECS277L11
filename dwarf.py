import character

class Dwarf(character.Character):
  """Concrete class for Dwarf
  Attributes: 
  abilities - list of abilities [0, 1, 0, 0]
  constitution - int of constitution
  strength - int of strength
  wisdom - int of wisdom"""
  def __init__(self, name):
    super().__init__(name + " the Dwarf")

  def abilities(self):
    return [0, 1, 0, 0]  # Archery, Fighting, Fire, Healing

  def constitution(self):
    return 13

  def strength(self):
    return 15

  def wisdom(self):
    return 10