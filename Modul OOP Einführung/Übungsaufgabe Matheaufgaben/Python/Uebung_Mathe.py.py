def addierer(num1, num2):
    ergebnis = int(num1) + int(num2)
    print("Rechnung : " + num1 + " + " + num2 + " = " + str(ergebnis))


def quadrat(number):
    ergebnis = int(number) * int(number)
    print("Rechnung : " + number + "²" + " = " + str(ergebnis))


def pruefung(number):
    if int(number) < 0:
        return False
    else:
        return True


def fakultaet(number):
    if number == 1:
        return 1
    else:
        return number * fakultaet(number - 1)


def main():
    print("Willkommen!")
    print("Wählen sie eine Option!")
    print("1 - Addierer")
    print("2 - Quadrieren")
    print("3 - Prüfen")
    print("4 - Fakultät")

    option = input("Ihre Eingabe: ")

    if option == '1':
        print("Bitte geben sie zwei Zahlen ein!")
        num1 = input("Zahl eins: ")
        num2 = input("Zahl zwei: ")
        addierer(num1, num2)
    elif option == "2":
        print("Bitte geben sie eine Zahl ein!")
        number = input("Ihre EIngabe: ")
        quadrat(number)
    elif option == "3":
        print("Bitte geben sie eine Zahl ein!")
        number = input("Ihre Eingabe: ")
        if pruefung(number):
            print("Die Zahl ist positiv!")
        else:
            print("Die Zahl ist negativ!")
    elif option == "4":
        print("Bitte geben sie eine Zahl ein!")
        number = int(input("Ihre Eingabe: "))
        if pruefung(number):
            ergebnis = fakultaet(number)
            print("Ihr Ergebnis: " + str(ergebnis))
        else:
            print("Zahl ist negativ! Nicht Möglich!")
    else:
        print("Ungültige Eingabe!")


main()
