import random
def play_game():
    tries = 0

    secret_number = random.randint(1,100)
    #print(f"psss, the secret number is {secret_number}")
    print("Welcome! Guess the secret number")

    difficulty = input("chose your difficulty, type 'h' for Hard or 'e' for Easy\n")
    game_over = False
    if difficulty == 'h':
        tries =10
    elif difficulty == 'e':
        tries = 15

    while tries > 0 and  not game_over :

        userGuess = int(input('Guess a number between 1 and 100\n'))

        if(userGuess == secret_number):
            
            print(f"You got it!! you win!")
            game_over = True
        elif(userGuess < secret_number):
            tries -=1
            print(f"Too low, you still can try {tries}more time(s)")
        elif(userGuess> secret_number):
            tries -=1
            print(f"Too High, you still can try {tries}more time(s)")               

    if tries == 0 :
        print("You ran out of tries. Better luck next time")
        


while input("Would you like to play a guessing game? type 'y' or 'n' \n") == 'y': 
    play_game()       