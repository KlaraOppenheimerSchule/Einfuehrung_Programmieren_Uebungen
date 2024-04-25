# Verwendung eines Dictionaries, um jede Episode zu repräsentieren
episodes = [
    {
        "Nr.": 1,
        "Titel": "Es weihnachtet schwer",
        "Originaltitel": "Simpsons Roasting on an Open Fire",
        "Dt. Erstausstrahlung": "6. Dez. 1991"
    },
    {
        "Nr.": 2,
        "Titel": "Bart wird ein Genie",
        "Originaltitel": "Bart the Genius",
        "Dt. Erstausstrahlung": "20. Sept. 1991"
    },
    {
        "Nr.": 3,
        "Titel": "Der Versager",
        "Originaltitel": "Homer’s Odyssey",
        "Dt. Erstausstrahlung": "11. Okt. 1991"
    },
    {
        "Nr.": 4,
        "Titel": "Eine ganz normale Familie",
        "Originaltitel": "There’s No Disgrace Like Home",
        "Dt. Erstausstrahlung": "13. Sep. 1991"
    }
]

# Ausgabe des Inhalts
for episode in episodes:
    print(f"Nr. {episode['Nr.']}:\n"
          f"   Titel: {episode['Titel']}\n"
          f"   Originaltitel: {episode['Originaltitel']}\n"
          f"   Dt. Erstausstrahlung: {episode['Dt. Erstausstrahlung']}\n"
          f"{'=' * 30}\n")
