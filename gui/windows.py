from tkinter import *

window = Tk()  # instantiate an instance of window
window.geometry("600x600")
window.title("PayTona.cc")
icon = PhotoImage(file="paytona_logo.png")
window.iconphoto(True, icon)
window.config(background="black")


window.mainloop()  # place windows on computer screen, listen events

# widgets = GUI elements: buttons, textboxes, labels, images

# windows = serves as a container to hold or contain the widgets
