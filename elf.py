import character

class Elf(character.Character):
  """ Abstract class for an elf.
  Attributes:
    _name - string name of the elf
  Functions
    abilities - list of abilities [0, 0, 1, 0]
    construction - int of constitution
    strength - int of strength
    wisdom - int of wisdom """
  def __init__(self, name):
    super().__init__(name + " the Elf")

  def abilities(self):
    return [0, 0, 1, 0]  # Archery, Fighting, Fire, Healing

  def constitution(self):
    return 10

  def strength(self):
    return 10
    
  def wisdom(self):
    return 15
    