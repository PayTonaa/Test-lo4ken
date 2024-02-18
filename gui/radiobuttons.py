# to samo co checkbox tylko mozna kliknac tylko jeden

from tkinter import *

food = ["pizza", "hamburger", "hotdog"]
window = Tk()

x = IntVar()

for index in range(len(food)):
    radiobutton = Radiobutton(window,
        text=food[index], #adds text to radio buttons
        variable=x, #groups radiobuttons together if they share t th
        value=index, #assigns each radiobutton a different value
        padx=25,image_=_food1,
        image = foodImages[index], #adds image to radiobutton
        compound_='left')#Madds image & text (left-side)))#Radds padding on x-axis


font=("Impact",50),

radiobutton.pack(anchor=W)
window.mainloop()