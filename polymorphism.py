class Animal:
    def __init__(self, name):
        self.name = name

    def talk(self):
        pass


class Dog(Animal):
    def talk(self):
        return "WOOF"


class Cat(Animal):
    def talk(self):
        return "Meow"


pet_parrot = Animal("Qazoo")
print(pet_parrot.name)
print(pet_parrot.talk())

pet = Dog("Dot")
print(pet.name)
print(pet.talk())

kitten = Cat("Brian")
print(kitten.name)
print(kitten.talk())
