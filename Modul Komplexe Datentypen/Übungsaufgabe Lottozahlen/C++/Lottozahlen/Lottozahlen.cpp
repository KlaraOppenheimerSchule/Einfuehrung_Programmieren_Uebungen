#include <iostream>
#include <random>
using namespace std;

//Aufgabenstellung:
//[x] Erstellen Sie ein Programm, das die Ziehung der Lottozahlen simuliert.
//Füllen Sie zunächst ein Array mit sechs Zahlen, die zufällig über folgenden Befehl erzeugt werden: rand() % 49 + 1;
//[ ] Erstellen Sie eine Methode, die die Überprüfung der Zahlen selbstständig ausführt.


void generateNumbers(){
    int randomNumbers[6];
    srand(time(NULL));
    for (int i : randomNumbers){
        i = rand() % 49 + 1;
        cout << i << " ";
            }
    }

void giveFeedback(){
    if(true){
        cout << endl << "Glückwunsch, Sie haben gewonnen";
    }
    else{
        cout << endl << "Leider verloren";
    }
}

int main(){
    int userNumbers[6];
    int userNumber;
    cout << "Bitte geben Sie ihre Zahlen einzeln ein:" << endl;
    for (int i = 0; i < 6;){
                cin >> userNumber;
        userNumbers[i] = userNumber;
        i++;
    }
cout << endl << "Lottozahlen:" << endl;
    generateNumbers();
    cout << endl << "Nutzereingabe:" << endl;
    for (int i : userNumbers){
        cout << i << " ";
            }
        return 0;
}