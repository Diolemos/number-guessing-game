<?php
function playGame(){
    $tries = 0;
$secretNum = rand(1,100);
$isGameOver = false;
$difficulty = (string)readline("Chose your difficulty. type 'h' for Hard, or 'e' for Easy  \n  ");

if($difficulty == 'h'){
    $tries = 10;
}elseif($difficulty == 'e'){
    $tries = 15;
}

while($tries>0 and $isGameOver == false){
    $userGuess = (integer)readline("Guess a number Between 1 and 100... \n ");

    if($userGuess == $secretNum){
        echo"Bulls eyes!!You win!!\n";
        $isGameOver = true;
    }elseif($userGuess < $secretNum){
        $tries--;
        echo"Too low!!\n, You still can try {$tries} time(s) \n";

    }elseif($userGuess > $secretNum){
        $tries--;
        echo"Too High!!\n, You still can try {$tries} time(s) \n";

    }
if($tries == 0){
    echo"Sorry, You ran out of tries.\n tip: Have you ever heard of 'binary search algorithm'? \n";
}    
}
}

while((string)readline("Would you like to play a guessing game? 'y' or 'n' \n\n") == 'y' ){
    playGame();
}