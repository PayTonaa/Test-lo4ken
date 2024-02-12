#Touple = collection which is ordered and unchangeable used to group together related data
# Co to jest Tuple?
# Krotki (tuples) to uporządkowane kolekcje dowolnych obiektów. Są heterogeniczne i mogą być dowolnie zagnieżdżane. Dostęp do obiektów możliwy jest za pomocą offsetu. Krotki są niezmiennymi sekwencjami, jak łańcuchy.
student = ("Bartek", 21, "Mężczyzna")

print(student.count("Bartek"))
print(student.index(21))
for x in student:
    print(x)

if "Bartek" in student:
    print("Bartek is here")