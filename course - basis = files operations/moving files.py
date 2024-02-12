import os

source = 'test.txt'
destination = ('C:\\Users\\bar-t\\Desktop\\test.txt')

try:
    if os.path.exists(destination):
        print("there is already there")
    else:
        os.replace(source,destination)
        print("sorce was moved")

except FileNotFoundError:
    print(":nie ma pliku")