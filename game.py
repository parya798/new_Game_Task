import random

def guess_number(secret_number, attempts=5):
    attempts_left = attempts
    while True:
        user_guess = input("the number is between (1 to 10), you have 5 chances: ")
        
        try:
            user_guess = int(user_guess)
        except ValueError:
            print("please add a number")
            continue
        
        if user_guess < secret_number:
            print("too little")
        elif user_guess > secret_number:
            print("too big")
        else:
            print("congrats! you guessed the number")
            return
    
        attempts_left -= 1
        if attempts_left == 0:
            print(f"sorry! out of chances, the number is: {secret_number}")
            break
    
def play_game():
    while True:
        secret_number = random.randint(1, 10)
        print("The game had begun, guess your number!")
        guess_number(secret_number, 3)
        
        play_again = input("do you wanna play again? (yes/no)")
        if play_again.lower() != "yes":
            break
        
play_game()