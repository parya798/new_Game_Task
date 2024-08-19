import random

def guess_number(secret_number, attempts=5):
    for attempt in range(attempts):
        user_guess = int(input("the number is between (1 to 10): 6"))
        
        if user_guess < secret_number:
            print("too little")
        elif user_guess > secret_number:
            print("too big")
        else:
            print("congrats! you guessed the number")
            return
    
    print(f"sorry! out of chances: {secret_number}")
    
def play_game():
    secret_number = random.randint(1, 10)
    attempts = 5
    print("The had begun, guess your number!")
    guess_number(secret_number, attempts)
    
play_game()