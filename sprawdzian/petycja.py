from tkinter import Tk, Text, Scrollbar, font, Button

def close_window():
    window.destroy()

window = Tk()
window.geometry("800x600")
window.title("PayTona.cc/main/prośba")
window.config(background="black")

code_text = """
Dzień dobry, chciałbym mieć możliwość również wyjaśnienia co robi 
po kolei każda linika tego kodu, gdyż polecenie było dla mnie lekko 
niejasne i w przeciwieństwie do niektórych wiem co się w nim dzieje
i potrafie napisać wersję ze słownikiem samemu




class TaskList:
   def __init__(self):
       self.tasks = []

   def addTask(self, title, description, date, completed=False):
       self.tasks.append({
           'title': title,
           'description': description,
           'date': date,
           'completed': completed
       })

   def showTask(self, show_completed=True):
       for task in self.tasks:
           if task['completed'] == show_completed:
               print(f"Title: {task['title']}")
               print(f"Description: {task['description']}")
               print(f"Date: {task['date']}")
               print(f"Completed: {'Yes' if task['completed'] else 'No'}")
               print("-" * 30)

   def taskComplete(self, title):
       for task in self.tasks:
           if task['title'] == title:
               task['completed'] = True
               break

zadanie = TaskList()
tasks_data = [
   ["Zakupy spożywcze", "Kupić chleb i mleko", "2024-02-15", False],
   ["Przygotowanie prezentacji", "Przygotować prezentację na spotkanie", "2024-02-20", False],
   ["Sprzątanie mieszkania", "Wysprzątać pokój i umyć podłogę", "2024-02-18", True],
   ["Zakupy online", "Zamówić nowe buty i koszulkę", "2024-02-17", False],
   ["Nauka do egzaminu", "Powtórzyć materiał z matematyki", "2024-02-16", False]
]

for task_data in tasks_data:
   zadanie.addTask(*task_data)

zadanie.taskComplete("Zakupy spożywcze")

print("Nieukończone zadania:")
zadanie.showTask(show_completed=False)

print("\nUkończone zadania:")
zadanie.showTask(show_completed=True)
"""

scrollbar = Scrollbar(window)
scrollbar.pack(side="right", fill="y")

text_font = font.Font(family="Courier", size=12)
text_widget = Text(window, wrap="word", yscrollcommand=scrollbar.set, bg="black", fg="white")
text_widget.insert("1.0", code_text)
text_widget.pack(expand=True, fill="both")

scrollbar.config(command=text_widget.yview)

button_no = Button(window, text="NIE", command=close_window, bg="red", fg="white")
button_no.pack(side="bottom", fill="x")

window.mainloop()
