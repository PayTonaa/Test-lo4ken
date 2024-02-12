import os


path = "C:\\Users\\bar-t\\PycharmProjects\\main\\pliki\\test.txt"

if os.path.exists(path):
    print("That location exist!")
    if os.path.isfile(path):
        print('ur location is file')
    else:
        print("kys")
else:
    print("that location doesn`t exist")