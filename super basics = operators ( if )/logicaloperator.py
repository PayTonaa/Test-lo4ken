# logical operators (and, or, not) = used to check if two or more conditional statements is True
# not zminia true na false i odwrotnie
temp = int(input("jaka jest temperatura na dworeze? "))

if not(temp >= 0 and temp <= 30): # oba muszą być prawdą
    print("the temperature is good today")
    print("go outside!")

elif not(temp <0 or temp > 30): # odwraca czytamy to jako jezeli temperatura nie jest w przedziale to zró bto
    print("temperature is bad today! ")
    print("stay inside")
