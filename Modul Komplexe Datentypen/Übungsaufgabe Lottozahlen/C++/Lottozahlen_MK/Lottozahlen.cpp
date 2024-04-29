#include <iostream>
#include <vector>
#include <random>
using namespace std;

//Aufgabenstellung:
//[x] Erstellen Sie ein Programm, das die Ziehung der Lottozahlen simuliert.
//Füllen Sie zunächst ein Array mit sechs Zahlen, die zufällig über folgenden Befehl erzeugt werden: rand() % 49 + 1;
//Anmerkung: damit die Zahlen ausreichend "zufällig" sind,
//muss zunächst durch srand(time(NULL)) die auktuelle zeit als "Zufallsquelle" gewählt werden
//[x] Erstellen Sie eine Methode, die die Überprüfung der Zahlen selbstständig ausführt.

void giveFeedback(bool win){
    if(win){
        cout << endl << "Glückwunsch, Sie haben gewonnen";
    }
    else{
        cout << endl << "Leider verloren";
    }
}

void checkNumbers(int userNumbers[], int randomNumbers[]){
    vector<int> equalNumbers;
    bool win;
    for (int i = 0; i < 6; i++)
    {
        if (userNumbers[i] == randomNumbers[i])
        {
            equalNumbers.push_back(userNumbers[i]);
        }
    }
    if (equalNumbers.size() == 6){win = true;}
    else{win = false;}

    giveFeedback(win);
}

vector<int> generateNumbers(){
    srand(time(NULL));
    vector<int> randomNumbers(6);
    for (int& i : randomNumbers){
        i = rand() % 49 + 1;
        cout << i << " ";
    }
    return randomNumbers;
}

bool isValidNumber(int number) {
    return number >= 1 && number <= 49;
}

int main(){
    int userNumbers[6];
    int userNumber;
    cout << "Bitte geben Sie ihre Zahlen einzeln ein:" << endl;
    for (int i = 0; i < 6;){
        cin >> userNumber;
        if (isValidNumber(userNumber)){
            userNumbers[i] = userNumber;
            i++;
        }
        else{ 
            cout << "Ungültige Eingabe. Bitte geben sie eine Zahl zwischen 1 und 49 ein." << endl;
        }
    }
    cout << endl << "Lottozahlen:\n";
    vector<int> randomNumbers = generateNumbers();
    cout << endl << "Nutzereingabe:\n";
    for (int i : userNumbers){
        cout << i << " ";
    }
    checkNumbers(userNumbers, randomNumbers.data());
    return 0;
}