# **kwargs = parameter that will pack all arguments into a dictionary useful so that a function can accept a varying amount of keyword arg


def hello(**kwargs):
    print("helo" + kwargs['first'] + " " + kwargs['last'])
    for key,value in kwargs.items():
        print(value)

hello(first="bro", last = "nigga")