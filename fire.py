import decorator

class Fire(decorator.Decorator):
  """ Concrete class for a fire ability.
  Functions:
    abilitiy - adds 1 to the character's fire ability
    constitution - subtracts 3 to the character's constitution
    strength - subtracts 1 to the character's strength
    wisdom - adds 5 to the character's wisdom"""
  def abilities(self):
    ability = super().abilities()
    ability[2] += 1
    return ability

  def constitution(self):
    return super().constitution() - 3

  def strength(self):
    return super().strength() - 1

  def wisdom(self):
    return super().wisdom() + 5