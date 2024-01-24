#include <iostream>
#include <random>
using namespace std;

//Aufgabenstellung:
//[x] Erstellen Sie ein Programm, das die Ziehung der Lottozahlen simuliert.
//Füllen Sie zunächst ein Array mit sechs Zahlen, die zufällig über folgenden Befehl erzeugt werden: rand() % 49 + 1;
//[ ] Erstellen Sie eine Methode, die die Überprüfung der Zahlen selbstständig ausführt. 


bool checkNumbers(int randomNumbers[6], int userNumbers[6]){
    int j = 0;
    for (int i = 0; i < 6;){
        if(randomNumbers[i] == userNumbers[i]){
            j++;
        }
    }
    if (j == 6){
        return true;
    }
    return false;
}

void generateNumbers(int userNumbers[6]){
    srand(time(NULL));
    int randomNumbers[6];
    for (int i = 0; i < 6;){
        randomNumbers[i] = rand() % 49 + 1;
        cout << randomNumbers[i] << " ";
        i++;
    }
    checkNumbers(randomNumbers, userNumbers);
    //??? Dieses Ding die randomNumbers returnen lassen
}

int main(){
    int userNumbers[6];
    cout << "Bitte geben Sie ihre Zahlen einzeln ein:";
    for (int i = 0; i < 6;){
        int userNumber;
        cin >> userNumber;
        userNumbers[i] = userNumber;
        i++;
    }
    cout << endl << "Lottozahlen:" << endl;
    generateNumbers(userNumbers);
    cout << endl << "Nutzereingabe:" << endl;
    for (int i = 0; i < 6;){
        cout << userNumbers[i] << " ";
        i++;
    }
    if(checkNumbers){
        cout << endl << "Glückwunsch, Sie haben gewonnen";
    }
    else{
        cout << endl << "Leider verloren";
    }
    return 0;
}