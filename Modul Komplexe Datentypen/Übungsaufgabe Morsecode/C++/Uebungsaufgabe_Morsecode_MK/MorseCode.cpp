#include <iostream>
#include <map>
using namespace std;

//Primary:
//[x] Entwickle ein Programm, das Buchstaben in Morsecode übersetzt
//Speichern Sie hierzu einfach einen Buchstaben in einer Variablen und lassen Sie diesen sodann übersetzten.
//Secondary:
//[ ] Übersetzung ganzer wörter
//[ ] Übersetzung ganzer sätze



int main()
{
    map<char, string> morse_codes = {
        {'A', ".-"}, {'B', "-..."}, {'C', "-.-."}, {'D', "-.."}, {'E', "."}, {'F', "..-."},
        {'G', "--."}, {'H', "...."}, {'I', ".."}, {'J', ".---"}, {'K', "-.-"}, {'L', ".-.."},
        {'M', "--"}, {'N', "-."}, {'O', "---"}, {'P', ".--."}, {'Q', "--.-"}, {'R', ".-."},
        {'S', "..."}, {'T', "-"}, {'U', "..-"}, {'V', "...-"}, {'W', ".--"}, {'X', "-..-"},
        {'Y', "-.--"}, {'Z', "--.."},
        {'1', ".----"}, {'2', "..---"}, {'3', "...--"}, {'4', "....-"}, {'5', "....."},
        {'6', "-...."}, {'7', "--..."}, {'8', "---.."}, {'9', "----."}, {'0', "-----"}
    };
    char letter;
    cout << "Welchen Buchstaben wollen Sie Uebersetzen?" << endl;
    cin >> letter;
    letter = toupper(letter);

    if (morse_codes.count(letter))
    {
        cout << "Der Buchstabe: " << letter << endl
        << "wird uebersetzt als: " << morse_codes.at(letter) << endl;
    }



    return 0;
}