super_euro_pro_liter = 1.43
diesel_euro_pro_liter = 1.22

def process():
    kraftstoffart = input("Bitte geben Sie den getankten Kraftstoff ein (1 = Super; 2 = Diesel): ")
    menge_in_liter = float(input("Bitte geben Sie die getankte Menge in Liter ein: "))

    modifikator = 0.95 if menge_in_liter >= 100 else 1

    match kraftstoffart:
        case '1':
            return super_euro_pro_liter * menge_in_liter * modifikator  
        case '2': 
            return diesel_euro_pro_liter * menge_in_liter * modifikator
        case _:
            print("Eingabe nicht Valide, wählen Sie eine der möglichen Kraftstoffarten!")
            return process()
    
print(f"Sie zahlen {process()} €")