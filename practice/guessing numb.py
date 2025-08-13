import random
import os
import platform
from time import sleep
 
def clear_screen():
    """Clear the console screen in a cross-platform way"""
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')
 
def number_guessing_game():
    """Enhanced number guessing game with learning features"""
    clear_screen()
    print("Welcome to the Python Number Guessing Game!")
    print("-----------------------------------------\n")
   
    # Game configuration
    min_num = 1
    max_num = 10
    attempts = 3
    score = 0
   
    while True:
        # Generate random number
        secret_number = random.randint(min_num, max_num)
        print(f"Guess a number between {min_num} and {max_num}. You have {attempts} tries.")
       
        # Guessing loop
        for attempt in range(attempts):
            try:
                guess = int(input(f"Attempt {attempt + 1}: "))
               
                if guess == secret_number:
                    print("\n🎉 Congratulations! You guessed correctly! 🎉")
                    score += (attempts - attempt) * 10  # More points for fewer attempts
                    break
                elif guess < secret_number:
                    print("Too low! Try a higher number.")
                else:
                    print("Too high! Try a lower number.")
                   
            except ValueError:
                print("Please enter a valid number!")
                continue
        else:
            print(f"\nSorry, you've used all your attempts. The number was {secret_number}.")
       
        # Show score and ask to play again
        print(f"\nYour current score: {score}")
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again not in ['yes', 'y']:
            print(f"\nThanks for playing! Your final score is {score}.")
            break
       
        clear_screen()
 
# Start the game
if __name__ == "__main__":
    number_guessing_game()