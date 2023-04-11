from colorama import Fore, Back, Style
print(Back.CYAN)
print(Fore.BLACK)
class Pet:

   def __init__(self, name, species):

       self.name = name

       self.species = species

       self.is_alive = True

       self.age = 0

   def grow(self):

       self.age += 1

cat = Pet("Яша", "кошка")

dog = Pet("Шарик", "собака")

cat.grow()

dog.grow()

print(f"{cat.name} растет и ему уже {cat.age} года")

print(f"{dog.name} растет и ему уже {dog.age} года")