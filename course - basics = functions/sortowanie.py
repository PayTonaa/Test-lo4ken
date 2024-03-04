
import random
# def sortuj(tab):
#     n = len(tab)
#     ile = 0
#     for i in range(n):
#         for j in range(0, n-i-1):
#          ile += 1
#             if tab[j] > tab[j+1]:
#                 tab[j], tab[j+1] = tab[j+1], tab[j]
#
# tablica = []
# for x in range(10):
#     tablica.append(random.randint(0, 100000))
# print(tablica)
# sortuj(tablica)
# print(tablica)


def sortuj2(tab):
    n = len(tab)
    ile = 0
    for i in range(n):
        lmin = i
        for j in range(i + 1, n):
            ile += 1
            if tab[j] < tab[lmin]:
                lmin = j

        tab[i], tab[lmin] = tab[lmin], tab[i]
    return ile

tab = []
for x in range(10):
    tab.append(random.randint(0, 100000))
print(tab)
sortuj2(tab)
print(sortuj2(tab))
print(tab)
