import random

x = random.randint(1,6) # tworzy randomową liczbe w zakresie
y = random.random()
print("twoja liczba to {:.2f}".format(y))
print(x)

mylist = ["kamień", 'papier', 'nozyce']

z= random.choice(mylist) # Funkcja choice losowo wybiera pojedynczy element z sekwencji (na przykład z listy) i zwraca ten element.
# Oryginalna lista lub sekwencja nie jest modyfikowana.


cards = [1,2,3,4,5,6,7,8,9, "J", "Q", "K", "A"]
random.shuffle(cards) #Funkcja shuffle losowo miesza elementy listy na miejscu, czyli zmienia kolejność elementów wewnątrz oryginalnej listy.
# Po użyciu shuffle, oryginalna lista zostaje zmodyfikowana.
print(z)

