import abc
import character


class Decorator(character.Character, abc.ABC):
  """ Decorator class to pass abilities.
  Attributes:
    _character - the character to be decorated
  Functions:
    abilities(): returns the character abilities
    constitution(): returns the character constitution
    strength(): returns the character strength
    wisdome(): returns the character wisdom
    """
  def __init__(self, c):
    super().__init__(c.name)
    self._character = c

  def abilities(self):
    return self._character.abilities()

  def constitution(self):
    return self._character.constitution()

  def strength(self):
    return self._character.strength()

  def wisdom(self):
    return self._character.wisdom()