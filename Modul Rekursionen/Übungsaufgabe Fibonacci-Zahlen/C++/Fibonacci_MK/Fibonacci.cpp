#include <iostream>
#include <string>
#include <vector>

//Erstellen Sie eine rekursive Lösung für die Berechnung der Fibonacci-Zahlen.
//Geben Sie für eine übergebene Zahl deren Fibonacci-Reihe aus. Z.B. für fib(7)= 1,1,2,3,5,8,13

std::vector<int> ergebnisse;

int fib(const int& n){

    int ergebnis;

    if(n <= 0){
        ergebnis = 0;
    }    
    else if(n == 1){
        ergebnis = 1;
        std::cout << ergebnis;
    }
    else{
        ergebnis = fib(n-2)+fib(n-1);
        std::cout << ", " << ergebnis;
    }

    return ergebnis;
}

int main(){
    int stellen;
    std::cout << "wie viele Zahlen wollen Sie ausgeben?" << std::endl;
    std::cin >> stellen;

    fib(stellen);

    return 0;
}