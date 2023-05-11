#include <iostream>
#include <string>
#include <cstdlib> 
#include <ctime> 
using namespace std;
void play_game(){
        
         cout<< "Welcome.";
    srand(time(nullptr));
    int randomNumber = rand() % 100 + 1;
    int tries = 0;
    int userGuess;
    char difficulty ;

    bool isGameOver = false;


    // Ask user for difficulty
    cout<< "Chose The difficulty. Type 'h' for Hard or 'e' for Easy.";
    cin >> difficulty;
    if(difficulty == 'h'){
        tries = 10;
    }else if(difficulty == 'e'){
        tries = 15;
    }

    while (tries > 0 and isGameOver == false){
        cout<< "Chose a number between 1 and 100 \n";
        cin>> userGuess ;
        
        if(userGuess == randomNumber){
            cout<<"You got it!! the answer is" <<userGuess;
            isGameOver = true;
        }else if(userGuess < randomNumber){
            tries --;
           cout << "Too low, you can still try " << tries << " time(s)";

        }else if(userGuess > randomNumber){
            tries --;
           cout << "Too High, you can still try " << tries << " time(s)";

        }
    }

    if(tries == 0){
        cout<<"You ran out of tries. Better luck next time.";
    }
    }
int main()
{   char wannaPlay ;
    cout<<"Would you like to play a guessing game? 'y' or 'n'";
    cin>>wannaPlay;
    while(wannaPlay == 'y'){
        play_game();
        cout<<"Would you like to play again? 'y' or 'n'?";
        cin>>wannaPlay;

    }
    return 0;
    
   
}