class Fighter:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.damage = 10

    def attack(self, other_guy):
        other_guy.health = other_guy.health - self.damage
        print("{} attacks {}!".format(self.name, other_guy.name))
        print("{} loses {} health points!".format(other_guy.name, self.damage))

    def __str__(self):
        return "{}: {}".format(self.name, self.health)

Narendra = Fighter("Narendra")
naren = Fighter("Naren")

print(Narendra)  # Narendra: 100
print(naren)

naren.attack(Narendra)
print(Narendra)

class Boxer(Fighter):
    def heal(self):
        self.health += 10


boxer_naren = Boxer("Boxer Qazi")
print(boxer_naren)
print(boxer_naren.damage)
print(boxer_naren.health)

boxer_naren.heal()

print(boxer_naren)
