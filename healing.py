import decorator


class Healing(decorator.Decorator):
  """ Concrete class for a healing ability.
  Functions:
    abilitiy - adds 1 to the character's healing ability
    constitution - adds 3 to the character's constitution
    strength - subtracts 4 to the character's strength
    wisdom - adds 2 to the character's wisdom"""
  def abilities(self):
    ability = super().abilities()
    ability[3] += 1
    return ability

  def constitution(self):
    return super().constitution() + 3

  def strength(self):
    return super().strength() - 4
  
  def wisdom(self):
    return super().wisdom() + 2
  