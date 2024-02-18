from tkinter import *
#label = and area widget that holds text and / or an image within a window
window = Tk()

photo = PhotoImage(file='paytona_logo.png')

label = Label(window, text="Hello my dear",
              font = ('Arial', 40, 'bold'),
              fg = "green",
              bg="black",
              relief=RAISED,
              bd=10,
              padx=20,
              pady=20,
              image=photo,
              compound='bottom')
label.pack()
# label.place(x=100, y=100)
window.mainloop()
