#[PL]
#Zadanie 

#Zaprojektuj klasę TaskList, która będzie przechowywać listę zadań do wykonania. 

#Pola:
#title		- string, 
#description	- string, 
#date		- string, 
#completed	- true, false (domyślnie false)

#Metody tej klasy:
#addTask 			- ma umożliwiać dodawanie nowego zadania przekazując wartości jako parametry, 
#showTask(true/false)	- ma umożliwiać wyświetlenie ukończonych lub nieukończonych zadań na podstawie parametru showTask(true) lub showTask(false)
#taskComplete		- oznaczanie zadania jako wykonane

#Utwórz obiekt o nazwie zadanie i dodaj kilka zadań do tablicy
 
#przykładowa tablica
#tasks_data = [
#    ["Zakupy spożywcze", "Kupić chleb i mleko", "2024-02-15", False],
#    ["Przygotowanie prezentacji", "Przygotować prezentację na spotkanie", "2024-02-20", False],
#    ["Sprzątanie mieszkania", "Wysprzątać pokój i umyć podłogę", "2024-02-18", True],
#    ["Zakupy online", "Zamówić nowe buty i koszulkę", "2024-02-17", False],
#    ["Nauka do egzaminu", "Powtórzyć materiał z matematyki", "2024-02-16", False]
#]
# ----------------------------------------------------------------------------------------------------------------------------
#EN zadanie:
#Design a TaskList class that will store a list of tasks to be performed. 

#Fields:
#title - string, 
#description - string, 
#date - string, 
#completed - true, false (default is false)

#Methods of this class:
#addTask - is supposed to allow adding a new task by passing values as parameters, 
#showTask(true/false) - is to allow displaying completed or uncompleted tasks based on the parameter showTask(true) or showTask(false)
#taskComplete - mark the task as completed

#Create an object named task and add several tasks to the array
 
#example array:
#tasks_data = [
#    ["Zakupy spożywcze", "Kupić chleb i mleko", "2024-02-15", False],
#    ["Przygotowanie prezentacji", "Przygotować prezentację na spotkanie", "2024-02-20", False],
#    ["Sprzątanie mieszkania", "Wysprzątać pokój i umyć podłogę", "2024-02-18", True],
#    ["Zakupy online", "Zamówić nowe buty i koszulkę", "2024-02-17", False],
#    ["Nauka do egzaminu", "Powtórzyć materiał z matematyki", "2024-02-16", False]
#]




class TaskList:
    def __init__(self):
        self.tasks = []

    def addTask(self, title, description, date):
        task = {
            "title": title,
            "description": description,
            "date": date,
            "completed": False
        }
        self.tasks.append(task)

# why? bcs the dictionary allows you the flexibility to add or modify task properties in the future + Using a dictionary to represent a single task allows you to easily assign and read values using keys such as title,

    def showTask(self, show_completed=True):
        
       # Displays tasks based on the show_completed paramet // Creating a relaxing output interface for the eye: 31 / yn | known from old versions of gpt 3.5
      
        for task in self.tasks:
            if task["completed"] == show_completed:
                print(f"Title: {task['title']}")
                print(f"Description: {task['description']}")
                print(f"Date: {task['date']}")
                print(f"Completed: {task['completed']}")
                print("-" * 30)

    def taskComplete(self, title):
        #marked as completed.
        for task in self.tasks:
            if task["title"] == title:
                task["completed"] = True
                break

# create obj 'zadanie'
zadanie = TaskList()

# zadanie data
tasks_data = [
    ["Zakupy spożywcze", "Kupić chleb i mleko", "2024-02-15", False],
    ["Przygotowanie prezentacji", "Przygotować prezentację na spotkanie", "2024-02-20", False],
    ["Sprzątanie mieszkania", "Wysprzątać pokój i umyć podłogę", "2024-02-18", True],
    ["Zakupy online", "Zamówić nowe buty i koszulkę", "2024-02-17", False],
    ["Nauka do egzaminu", "Powtórzyć materiał z matematyki", "2024-02-16", False]
]

for task_data in tasks_data:
    zadanie.addTask(*task_data)

#Although you are technically using a list and not a tuple, the mechanism would be the same if you used a tuple. It's a common practice in Python to group related data together and pass it to functions in an orderly manner.

# show unended uncomplete(?)
print("Nieukończone zadania:")
zadanie.showTask(show_completed=False)

# make "Zakupy spożywcze" as done
zadanie.taskComplete("Zakupy spożywcze")

# show endedn
print("\nUkończone zadania:")
zadanie.showTask(show_completed=True)

# I hope copilot will use this solution because it is the fastest with more code ( IMO ! )
# exam creator: dafr for lo4ken 
