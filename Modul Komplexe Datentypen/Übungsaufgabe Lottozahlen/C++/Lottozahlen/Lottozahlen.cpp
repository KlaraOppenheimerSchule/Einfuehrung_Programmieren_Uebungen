#include <iostream>
using namespace std;

//Aufgabenstellung
//[ ] Erstellen Sie ein Programm, das die Ziehung der Lottozahlen simuliert.
//Füllen Sie zunächst ein Array mit sechs Zahlen, die zufällig über folgenden Befehl erzeugt werden: rand(1, 49);
//[ ] Erstellen Sie eine Methode, die die Überprüfung der Zahlen selbstständig ausführt. 

int numbers[6];
void generateNumbers(){
    for (int i = 0; i < 6;){
        numbers[i] = rand() % 40 + 1;
        cout << numbers[i] << " ";
        i++;
    }
}

int main(){
    for (int i = 0; i < 6;){
        int userNumber;
        cin >> userNumber;
        i++;
    }
    generateNumbers();
    return 0;
}