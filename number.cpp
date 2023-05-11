#include <iostream>
#include <string>
#include <cstdlib> 
#include <ctime> 
using namespace std;

int main()
{
    cout<< "Welcome.";
    srand(time(nullptr));
    int randomNumber = rand() % 100 + 1;
    int tries = 0;
    char difficulty ;

    bool isGameOve = false;


    // Ask user for difficulty
    cout<< "Chose The difficulty. Type 'h' for Hard or 'e' for Easy.";
    cin >> difficulty;
    if(difficulty == 'h'){
        tries = 10;
    }else if(difficulty == 'e'){
        tries = 15;
    }

    
}