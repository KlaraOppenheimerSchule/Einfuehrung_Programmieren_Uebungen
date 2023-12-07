#include <iostream>
#include <algorithm>
using namespace std;

//initializing variables

bool isLeapYear;
int year;

//Checks wether the entered year is a leap year.
void checkLeapYear(int year){
    if (year % 4 == 0 && year % 100 != 0){
        isLeapYear = true;
    }
    else if(year % 400 == 0){
        isLeapYear = true;
    }
    else{
        isLeapYear = false;
    }
}

string string_tolower(string s){
    transform(s.begin(), s.end(), s.begin(),
    [](unsigned char c){return tolower(c);});
    return s;
}

int main(){
    string input;
    cout << "What year would you like to check: ";
    cin >> year;
    checkLeapYear(year);
    if (isLeapYear == false){
        cout << "\n" << year << " is not a leap year.\nwould you like to check another year? (y/n)";
        cin >> input;
    }
    else{
        cout << "\n" << year << " is a leap year.\nwould you like to check another year? (y/n)";
        cin >> input;
    }
    if (string_tolower(input) == "y"){
        main();
    }
    return 0;
}