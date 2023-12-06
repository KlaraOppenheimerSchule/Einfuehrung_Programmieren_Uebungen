import unittest

def process():
    punkte = float(input("Punktzahl: "))

    if 87 <= punkte <= 100:
        print("1")
    elif 74 <= punkte <= 86:
        print("2")
    elif 59 <= punkte <= 73:
        print("3")
    elif 41 <= punkte <= 58:
        print("4")
    elif 6 <= punkte <= 40:
        print("5")
    elif 0 <= punkte <= 5:
        print("6")
    else:
        print("Eingabe nicht Valide")
        process()

process()