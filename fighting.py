import decorator

class Fighting(decorator.Decorator):
  """ Concrete class for a fighting ability.
  Functions:
    abilitiy - adds 1 to the character's fighting ability
    constitution - adds 2 to the character's constitution
    strength - adds 2 to the character's strength
    wisdom - subtracts 3 to the character's wisdom"""
  def abilities(self):
    ability = super().abilities()
    ability[1] += 1
    return ability

  def constitution(self):
    return super().constitution() + 2

  def strength(self):
    return super().strength() + 2

  def wisdom(self):
    return super().wisdom() - 3