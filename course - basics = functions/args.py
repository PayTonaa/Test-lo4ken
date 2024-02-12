# args =
# parameter that will pack all arguments into a tuple useful so that a function
# can accept a varying amount of arguments

def add(*args):    #gwiazdka zbiera wszystko z dłu do jednego worka jako tuple ( krotka )
    sum = 0
    args = list(args)
    args[0] = 0
    for i in args:
        sum+=i
    return sum

print(add(1,2,3,4,5,6))