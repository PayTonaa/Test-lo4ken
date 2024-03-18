# tab[n] ← tablica n liczb
#
# dla każdego i=0..n-1 w tablicy wykonuj:
#
#   dla każdego j=0..n-1-i wykonuj
#
#     Jeśli tab[j] > tab[j+1] to
#
#  zamień tab[j] z tab[j+1]
#


import  random
def sort1(tab):
    n = len(tab)
    for i in range(n-1):
        for j in range(n-1-i):
            if tab[j] > tab[j+1]:
                tab[j], tab[j+1] = tab[j+1], tab[j]
    print(tab)


tab = []
for x in range(100):
    tab.append(random.randint(10,10000))
print(tab)
sort1(tab)



