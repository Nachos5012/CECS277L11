import dwarf
import elf
import halfing
import archery
import fighting
import fire
import healing
import check_input

def main():
  """
  Main program file for managing character abilities and stats.
  """
  print("Character Maker!")
  print("Choose your character: \n1. Dwarf\n2. Elf\n3. Halfing")
  choice = check_input.get_int_range("Enter choice: ", 1, 3)
  name = input("\nWhat is your character's name?  ")
  print()
  player = None
  if choice == 1:
    player = dwarf.Dwarf(name)
  elif choice == 2:
    player = elf.Elf(name)
  else:
    player = halfing.Halfing(name) 
  print(player)
  print("You have 5 points to spend:")
  points = 5
  while True:
    print("Add an ability: \n1. Archery\n2. Fighting\n3. Fire Magic\n4. Healing")
    ability = check_input.get_int_range("Enter ability: ", 1, 4)
    if ability == 1:
      player = archery.Archery(player)
    elif ability == 2:
      player = fighting.Fighting(player)
    elif ability == 3:
      player = fire.Fire(player)
    else:
      player = healing.Healing(player)
    print()
    print(player)
    points -= 1
    if player.constitution() <= 0 or player.strength() <= 0 or player.wisdom() <= 0:
      print("You have failed to complete your character.  Game over.")
      break
    if points == 0:
      print("Congratulations!  You have created your character.")
      break
  


if __name__ == "__main__":
  main()