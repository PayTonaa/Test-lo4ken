# exception =
# events detected during execution that interrupt the flow of a program
while True:
    try:
        numerator = int(input("wpisz numer do podzielenia"))
        denominator = int(input("wpisz numer którym chceszp odzielic: "))
        result = numerator / denominator
        print(result)

    except ZeroDivisionError as e:   # Ten obiekt zawiera szczegóły o tym, co poszło nie tak, w tym typ wyjątku
        # i komunikat o błędzie. Używając as e, mówisz Pythonowi,
        # żeby złapał wyjątek i przypisał go do zmiennej e
        print("u cant divide by zero")
        print(e)

    except ValueError as e:
        print("wpisz numry prosze")
        print(e)

    except Exception as e:
        print("something went wrong :(")
        print(e)
    else:           # else to jest takie jak: jezeli nie wyłapiesz zadnego błędu to zrób to
        break
    finally:        # zawsze sie wyswietli niezalecznie od wszystkiego
        print("paytna 1.0 tech")
print(result)