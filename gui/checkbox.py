from tkinter import*


def display():
    if(x.get()):
        print("You agree!")
    else:
        print("you dont agree")

window = Tk()
x = BooleanVar()
logo = PhotoImage(file='paytona_logo.png')
check_button = Checkbutton(window,
                           text = "i agree to sth",
                           variable = x,
                           onvalue = True,
                           offvalue = False,
                           command=display,
                           font = ('Arial',20),
                           fg="red",
                           bg = "black",
                           activebackground="black",
                           activeforeground="white",
                           padx = 25,
                           pady = 10,
                           image = logo,
                           compound= LEFT

                           )

check_button.pack()
window.mainloop()