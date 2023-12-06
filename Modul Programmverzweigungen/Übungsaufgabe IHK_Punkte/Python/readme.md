def notenschlüssel(punkte):
    if punkte <  0 or punkte > 100:
        return "Ungültiger Wert. Bitte gib deine Punkte richtig ein."
    elif punkte >= 92:
        return "Note: 1"
    elif punkte >= 81:
        return "Note: 2"
    elif punkte >= 67:
        return "Note: 3"
    elif punkte >= 50:
        return "Note: 4"
    elif punkte >= 30:
        return "Note: 5"
    else:
        return "Note: 6"

try:
    punkte = int(input("Wie viele Punkte hast du?"))
    print(notenschlüssel(punkte))
except ValueError:
    print("Ungültiger Wert. Bitte gib deine Punkte richitg ein.")
