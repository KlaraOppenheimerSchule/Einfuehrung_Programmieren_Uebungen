#include <iostream>
#include <vector>
#include <random>
using namespace std;

//Aufgabenstellung:
//[x] Erstellen Sie ein Programm, das die Ziehung der Lottozahlen simuliert.
//Füllen Sie zunächst ein Array mit sechs Zahlen, die zufällig über folgenden Befehl erzeugt werden: rand() % 49 + 1;
//Anmerkung: damit die Zahlen ausreichend "zufällig" sind,
//muss zunächst durch srand(time(NULL)) die auktuelle zeit als "Zufallsquelle" gewählt werden
//[ ] Erstellen Sie eine Methode, die die Überprüfung der Zahlen selbstständig ausführt.


int randomNumbers[6];

void giveFeedback(bool win){
    if(win){
        cout << endl << "Glückwunsch, Sie haben gewonnen";
    }
    else{
        cout << endl << "Leider verloren";
    }
}

void checkNumbers(int userNumbers[]){
    vector<int> equalNumbers;
    for (int i = 0; i < 6; i++)
    {
        if (userNumbers[i] = randomNumbers[i])
        {
            equalNumbers.push_back(userNumbers[i]);
        }
    }
    if (equalNumbers.size() == 6)
    {
        
    }
    
    return false;
}

void generateNumbers(){
    srand(time(NULL));
    for (int i : randomNumbers){
        i = rand() % 49 + 1;
        cout << i << " ";
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
    cout << endl << "Lottozahlen:\n";
    generateNumbers();
    cout << endl << "Nutzereingabe:\n";
    for (int i : userNumbers){
        cout << i << " ";
            }
        return 0;
    checkNumbers(userNumbers);
}