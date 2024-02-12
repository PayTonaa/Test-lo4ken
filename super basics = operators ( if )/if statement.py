# if statement = a block of code that will execute if it's condition is truel

age = float(input("ile masz lat?"))
age = int(age)

if age >= 18:
    print("You are an adoult")
    if age == 100:
        print("old man congs bro!")
elif age < 0:
    print("ints impossible! ")
else:
    print("ur child")
