# index operator [] = gives access to a sequence's element (str,list, tuples)

name = ("bartek Tost!")
name = name[:-1]
if name[0] .islower():
    name = name.capitalize()
firsname = name[:name.find(" ")].lower()
lastname = name[name.find(' '):].upper()

print(firsname, lastname)



