class File:
    def __init__(self):
        self.tasks = []

    def insertdata(self, id, name, surname, street, number, cl):
        self.tasks.append({
            'id': id,
            'name': name,
            'surname': surname,  # Corrected typo: 'urname' to 'surname'
            'street': street,    # Corrected typo: 'treet' to 'street'
            'number': number,
            'cl': cl
        })

    def count(self):
        classes = {}
        for task in self.tasks:
            cl = task['cl']
            if cl in classes:
                classes[cl] += 1
            else:
                classes[cl] = 1
        return classes


with open("z:\\daneOsobowe.txt") as plik:
    tab = plik.read().splitlines()

zadanie = File()

for arg in tab:
    id, name, surname, street, number, cl = arg.split(';')
    zadanie.insertdata(id, name, surname, street, number, cl)

total_people = zadanie.count()
print(f"Total number of people in each class: {total_people}")
