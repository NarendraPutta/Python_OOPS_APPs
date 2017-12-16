class Fighter:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.damage = 10

    def attack(self, other_guy):
        other_guy.health = other_guy.health - self.damage


Narendra = Fighter("Narendra")
naren = Fighter("Naren")

print(Narendra.name)
print(naren.name)

naren.attack(Narendra)
print(Narendra.health)
