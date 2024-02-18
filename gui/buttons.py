from tkinter import *


count = 0
def click():
    global count
    count += 1
    print(count)
    print("you clicked the button")

window = Tk()

photo = PhotoImage(file = 'paytona_logo.png')
button = Button(window,
                text="kliknij mnie!",
                command=click,
                font=("Comic Sans", 30),
                fg="white",
                bg = "black",
                activeforeground="red",
                activebackground="black",
                state=ACTIVE,
                image = photo,
                compound='left')
button.pack()
window.mainloop()