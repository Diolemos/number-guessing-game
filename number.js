const prompt = require("prompt-sync")();

const playGame = ()=>{
    console.log("welcome!")
secreteNumber = Math.floor(Math.random() * 100) + 1
let tries = 0
let isGameOve = false
// console.log(secreteNumber)

let difficulty = prompt("chose your difficulty, type 'h' for Hard or 'e' for Easy\n")

if(difficulty == 'h'){
    tries = 10
}else if(difficulty =='e'){
    tries = 15
}

while( tries > 0 && isGameOve == false){

    let userGuess = +prompt("Choose a number between 1 and 100 \n")

    if(userGuess == secreteNumber){
        console.log("You win!!Thank you for playing!")
        isGameOve = true
    }
    else if (userGuess < secreteNumber){
        tries--
        console.log(`Too low, you still can try ${tries} time(s)`)
    }
    else if(userGuess > secreteNumber){
        tries--
        console.log(`Too high, you can still try ${tries} time(s)`)
    }    
    }
if(tries == 0){
    console.log("You ran out of tries, better luck next time")
}

}

while( prompt("Would you like to play a guessing game? press 'y' or 'n' \n")=='y'){
    playGame()
}