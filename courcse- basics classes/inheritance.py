# mother classes gives atributes to child classes

class Animal:

    alive = True

    def eat(self):
        print("this animal is sleepieng")
    def sleep(self):
        print("this animal is sleeping")

class Rabbit(Animal): # child class of animal
    pass
class Fish(Animal):  # child class of animal
    pass
class Hawk(Animal):  # child class of animal
    pass

rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

print(rabbit.eat())
rabbit.eat()



