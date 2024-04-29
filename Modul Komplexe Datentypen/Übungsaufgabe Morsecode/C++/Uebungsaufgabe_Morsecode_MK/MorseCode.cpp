#include <iostream>
#include <map>
#include <algorithm>
using namespace std;

//Primary:
//[x] Entwickle ein Programm, das Buchstaben in Morsecode übersetzt
//Speichern Sie hierzu einfach einen Buchstaben in einer Variablen und lassen Sie diesen sodann übersetzten.
//Secondary:
//[x] Übersetzung ganzer wörter
//[ ] Übersetzung ganzer sätze

string translate(const string& str, const map<char, string>& morse_codes){
    string translated;
    for (char c : str){
        if (morse_codes.count(c)){
            translated.append(morse_codes.at(c));
        }
    }
    return translated;
}

string CAPSLOCK(const string& str, map<char, string>& morse_codes){  
    string stringCaps;
    for (char c : str){
        c = toupper(c);
        stringCaps.push_back(c);
    }
    return stringCaps;
}

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

    string toTranslate;
    cout << "Was wollen Sie Uebersetzen?" << endl;
    cin >> toTranslate;

    cout << "Die Eingabe:" << toTranslate << endl;

    toTranslate = CAPSLOCK(toTranslate, morse_codes);
    string translated = translate(toTranslate, morse_codes);

    cout << "wird uebersetzt als:" << translated << endl;

    return 0;
}