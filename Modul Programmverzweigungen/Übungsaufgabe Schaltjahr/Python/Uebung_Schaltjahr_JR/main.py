from Year import *

def main():

    print("Wilkommen beim Schaltjahrprogramm")
    print("___________________________________________")
    print("Bitte geben sie eine Jahreszahl ein!")
    inputYear = input("Eingabe: ")

    bool = Year.isSchaltjahr(inputYear)

    if bool:
        txt = "Das Jahr " + inputYear + " ist ein Schaltjahr!"
        print(txt)
    else:
        txt = "Das Jahr " + inputYear + "ist KEIN Schaltjahr"
        print(txt)


main()