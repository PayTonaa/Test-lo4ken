
try:
    with open('test.tx') as file:  # zamyka wszystko od razu po odczytaniu
        print(file.read())
except FileNotFoundError:
    print("filename is wrong")

