import decorator

class Archery(decorator.Decorator):
  """ Concrete class for a healing ability.
  Functions:
    abilitiy - adds 1 to the character's archery ability
    constitution - subtracts 2 to the character's constitution
    strength - adds 5 to the character's strength
    wisdom - subtracts 2 to the character's wisdom"""
  def abilities(self):
    ability = super().abilities()
    ability[0] += 1
    return ability

  def constitution(self):
    return super().constitution() - 2

  def strength(self):
    return super().strength() + 5

  def wisdom(self):
    return super().wisdom() - 2

  