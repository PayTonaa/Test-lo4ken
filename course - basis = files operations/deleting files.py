import os # standard usuwa pliki i puste foldery
import shutil # usuwa sie foldery które są pełne

path = 'copy.txt'


try:
    os.remove('copy.txt') # usuwa pliki
    os.rmdir(path) # usuwa puste foldery
    shutil.rmtree(path) # usuwa folder i wszystko co się w nim znajduje
except FileNotFoundError as e:
    print(e)
    print("No such file")
except PermissionError as e:
    print(e)
    print("u dont have perms")

# path.exists(path)