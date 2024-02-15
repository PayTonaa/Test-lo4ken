class Game:
    cache = []

    def __init__(self, id, name, category):
        self.id = id
        self.name = name
        self.category = category
        self.cache.append(self)

    def serchingcounting(self, gamename):
        for x in self.cache:
            if x.id == gamename:
                return x.name

    def serching(self):
        ids = []
        for catg in self.cache:
            if catg.category == "imprezowa":
                ids.append(catg.id)
        return ids

    def idtoname(self, game_ids):
        game_names = []
        for game_id in game_ids:
            pass


class Gamers:
    cache = []

    def __init__(self, id, name, surname, age):
        self.id = id
        self.name = name
        self.surname = surname
        self.age = age
        self.cache.append(self)

    def categoryfiltering(self):
        categ = {}
        for aged in self.cache:
            if int(aged.age) <= 19:
                categ[aged.id] = "Junior"
            elif int(aged.age) >= 20 and int(aged.age) <= 49:
                categ[aged.id] = "seniorzy"
            elif int(aged.age) > 49:
                categ[aged.id] = "weterani"
        return categ


class Rates:
    cache = []

    def __init__(self, gameid, gamerid, status, rank):
        self.gameid = gameid
        self.gamerid = gamerid
        self.rank = rank
        self.status = status
        self.cache.append(self)

    def counting(self):
        counts = {}
        for rate in self.cache:
            gameid = rate.gameid
            if gameid in counts:
                counts[gameid] += 1
            else:
                counts[gameid] = 1
        # issue finder GPT fixed this issue
        max_value = max(counts.values())
        max_key = max(counts, key=counts.get)

        return max_key

    def ratingavg(self, ids):
        reviews = {}
        for id in ids:
            score = 0
            count = 0
            for rate in self.cache:
                if rate.gameid == id:
                    if rate.gameid in reviews:
                        # reviews[rate.gameid] += int(rate.rank)
                        score += int(rate.rank)
                        count += 1
                    elif rate.gameid not in reviews:
                        reviews[rate.gameid] = 0
                        score += int(rate.rank)
                        count += 1
            reviews[id] += round(score/count, 2)
        return reviews

    def amountofplayers(self):
        reviewed = {}
        for player in self.cache:
            if player.gamerid in reviewed:
                if player.status == 'posiada':
                    reviewed[player.gamerid] = 1
                else:
                    pass
            if player.gamerid not in reviewed:
                if player.status == 'posiada':
                    reviewed[player.gamerid] = 1
                else:
                    reviewed[player.gamerid] = 0
        # issue finder GPT fixed this \|/
        zero_reviews_count = sum(
            1 for value in reviewed.values() if value == 0)
        return zero_reviews_count

    #     for ids, category in categories.items():
    #         for reviews in self.cache:
    #             if reviews.gamerid == ids:
    #                 # if category == 'Junior':
    #                 #     if ids not in junior:
    #                 #         junior[reviews.gameid] = 1
    #                 #     else:
    #                 #         junior[reviews.gameid] += 1
    #                 # if category == 'seniorzy':
    #                 #     if ids not in seniors:
    #                 #         seniors[reviews.gameid] = 1
    #                 #     else:
    #                 #         seniors[reviews.gameid] += 1
    #                 # if category == 'weterani':
    #                 #     if ids not in weterans:
    #                 #         weterans[reviews.gameid] = 1
    #                 #     else:
    #                 #         weterans[reviews.gameid] += 1
    #                 #   File "c:\Users\bar-t\PycharmProjects\main\courcse- basics classes\database.py", line 124, in amountofreviewsweterans[reviews.gameid] += 1
    #                 #                                                                                                             ~~~~~~~~^^^^^^^^^^^^^^^^KeyError: '7'

    def amountofreviews(self, categories):
        junior = {}
        seniors = {}
        weterans = {}
        for ids, category in categories.items():
            for reviews in self.cache:
                if reviews.gamerid == ids:
                    if category == 'Junior':
                        junior.setdefault(reviews.gameid, 0)
                        junior[reviews.gameid] += 1
                    elif category == 'seniorzy':
                        seniors.setdefault(reviews.gameid, 0)
                        seniors[reviews.gameid] += 1
                    elif category == 'weterani':
                        weterans.setdefault(reviews.gameid, 0)
                        weterans[reviews.gameid] += 1
        # issue finder \|/
        max_junior = [(k, v) for k, v in junior.items() if v ==
                      max(junior.values())] if junior else None
        max_seniors = [(k, v) for k, v in seniors.items() if v ==
                       max(seniors.values())] if seniors else None
        max_weterans = [(k, v) for k, v in weterans.items()
                        if v == max(weterans.values())] if weterans else None

        return max_junior, max_seniors, max_weterans


plik = open("C:\\Users\\bar-t\\Documents\\Dane_2305\\gry.txt")
tab = plik.read().splitlines()
for line in tab:
    # issue finder: Sprawdzamy, czy linia zawiera przynajmniej trzy elementy po podziale za pomocą '\t'
    if len(line.split('\t')) >= 3:
        id, name, category = line.split('\t')
        zadanie = Game(id, name, category)
    else:
        print(f"Nieprawidłowa linia: {line}")

plik1 = open("C:\\Users\\bar-t\\Documents\\Dane_2305\\gracze.txt")
tab1 = plik1.read().splitlines()
for line in tab1:
    # isse finder: Podobnie, sprawdzamy, czy linia zawiera przynajmniej cztery elementy po podziale za pomocą '\t'
    if len(line.split('\t')) >= 4:
        id, name, surname, age = line.split('\t')
        zadanie1 = Gamers(id, name, surname, age)
    else:
        print(f"Nieprawidłowa linia: {line}")

plik2 = open("C:\\Users\\bar-t\\Documents\\Dane_2305\\oceny.txt")
tab2 = plik2.read().splitlines()
for line in tab2:
    # isse finder: Podobnie, sprawdzamy, czy linia zawiera przynajmniej cztery elementy po podziale za pomocą '\t'
    if len(line.split('\t')) >= 4:
        gameid, gamerid, status, rank = line.split('\t')
        zadanie2 = Rates(gameid, gamerid, status, rank)
    else:
        print(f"Nieprawidłowa linia: {line}")

gamename = zadanie2.counting()
print(zadanie.serchingcounting(gamename))
ids = zadanie.serching()
print(ids)
print(zadanie2.ratingavg(ids))
categories = zadanie1.categoryfiltering()
print(zadanie2.amountofreviews(categories))
half = zadanie2.amountofreviews(categories)
print(zadanie.idtoname(half))
