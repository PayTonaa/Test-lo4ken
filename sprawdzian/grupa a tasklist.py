
class TaskList:
    title = ""
    description = ""
    date = ""
    completed = False
    def addTask(self, tittle, description, date, completed):
        self.tittle = tittle
        self.description = description
        self.date = date
        self.completed = completed
    def showTask(self, arg):
        if self.completed == arg:
            print(f"{self.description}, {self.tittle}, {self.date}, {self.completed}")
    def taskComplete(self):
        self.completed = True

tab = []
tasks_data = [
    ["Zakupy spożywcze", "Kupić chleb i mleko", "2024-02-15", False],
    ["Przygotowanie prezentacji", "Przygotować prezentację na spotkanie", "2024-02-20", False],
    ["Sprzątanie mieszkania", "Wysprzątać pokój i umyć podłogę", "2024-02-18", True],
    ["Zakupy online", "Zamówić nowe buty i koszulkę", "2024-02-17", False],
    ["Nauka do egzaminu", "Powtórzyć materiał z matematyki", "2024-02-16", False]
]

for task in tasks_data:
    zadanie = TaskList()
    zadanie.addTask(*task)
    tab.append(zadanie)

for task in tab:
    task.showTask(False)
print("")
for task in tab:
    task.showTask(True)

tittle1 =input("podaj nazwe")
for taks in tab:
    if taks.tittle == tittle1:
        taks.taskComplete()

for task in tab:
    task.showTask(True)
