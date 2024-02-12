# str.format() =
# optional method that gives users more control when displaying output

print("The {1} jumped over the {0}".format("cow", "moon")) # zatępuje {} paceholder dla wartości albo tekstu


print("The {animal} jumped over the {item}".format(animal = "cow", item = "moon")) # keyword argument

text = "the {animal} jumped over the {item}"
print(text.format(animal="cow", item = "moon"))

name = "Bartek"

print("Hello, my name is {}".format((name)))
print("Hello, my name is {:^10}".format((name))) # odstęp 5 spacji z obu stron 10 > z prawej 10 < z lewej

numbers = 3.14159
number = 1000
print("The pi is {:.2f}".format(numbers)) # zaokrągla do 2 miejsc po przecinku


print("The is {:,}".format(number)) # dodaje przecinki do 1000
print("The is {:,}".format(number)) # dodaje biarnie wszystko
print("The is {:b}".format(number)) # X = dziesiątkowy, b binarny i o ósemkowy