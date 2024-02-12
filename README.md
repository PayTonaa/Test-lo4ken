TEST POLECENIE 
[PL]
Zadanie

Zaprojektuj klasę TaskList, która będzie przechowywać listę zadań do wykonania.

Pola:
title		- string,
description	- string,
date		- string,
completed	- true, false (domyślnie false)

Metody tej klasy:
addTask 			- ma umożliwiać dodawanie nowego zadania przekazując wartości jako parametry,
showTask(true/false)	- ma umożliwiać wyświetlenie ukończonych lub nieukończonych zadań na podstawie parametru showTask(true) lub showTask(false)
taskComplete		- oznaczanie zadania jako wykonane

Utwórz obiekt o nazwie zadanie i dodaj kilka zadań do tablicy

przykładowa tablica
tasks_data = [
   ["Zakupy spożywcze", "Kupić chleb i mleko", "2024-02-15", False],
   ["Przygotowanie prezentacji", "Przygotować prezentację na spotkanie", "2024-02-20", False],
   ["Sprzątanie mieszkania", "Wysprzątać pokój i umyć podłogę", "2024-02-18", True],
   ["Zakupy online", "Zamówić nowe buty i koszulkę", "2024-02-17", False],
   ["Nauka do egzaminu", "Powtórzyć materiał z matematyki", "2024-02-16", False]
]

TEST:
EN zadanie:
Design a TaskList class that will store a list of tasks to be performed.

Fields:
title - string,
description - string,
date - string,
completed - true, false (default is false)

Methods of this class:
addTask - is supposed to allow adding a new task by passing values as parameters,
showTask(true/false) - is to allow displaying completed or uncompleted tasks based on the parameter showTask(true) or showTask(false)
taskComplete - mark the task as completed

Create an object named task and add several tasks to the array

example array:
tasks_data = [
   ["Zakupy spożywcze", "Kupić chleb i mleko", "2024-02-15", False],
   ["Przygotowanie prezentacji", "Przygotować prezentację na spotkanie", "2024-02-20", False],
   ["Sprzątanie mieszkania", "Wysprzątać pokój i umyć podłogę", "2024-02-18", True],
   ["Zakupy online", "Zamówić nowe buty i koszulkę", "2024-02-17", False],
   ["Nauka do egzaminu", "Powtórzyć materiał z matematyki", "2024-02-16", False]
]
