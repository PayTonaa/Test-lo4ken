# list = used to store multiple items in a single variable

food = ["pizza", "hotdog", "spagetti", "pudding"]
food[0] = "sushi" # zamienia
print(food[0])
food.append("ice cream") # dodaje na koniec
food.remove("hotdog") # usuwa określony
food.pop() # usuwa ostatnie
food.insert(0, "cake") # dodaje na miejscu o indeksie
food.sort() #sortuje
food.clear() # usuwa wszystko z listy
for x in food:
    print(x)
