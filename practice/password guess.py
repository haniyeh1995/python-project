import random

def generate_secret_code():
    digits = [str(random.randint(1, 9)) for _ in range(4)]
    return ''.join(digits)

secret_code = generate_secret_code()


def passwprd_guess():
    max_attemp = 3
    
    while True:
        attempt_left = max_attemp
        number = list(secret_code)
        guessed_number = []
        
        while attempt_left > 0 :
             display = ""
             for i in number:
                  if i in guessed_number:
                    display += i + " "
                  else:
                   display += " _ "
             print("password:", display.strip())
           
             if all(i in guessed_number for i in number):
                print("\n🎉 You won! The password was:", secret_code)
                break
             
             guess = input("Guess the password:(it is 4 digit number)\n")

             if len(guess) != 1 or not guess.isdigit():
                print("❗ Please enter only one number.")
                continue

             if guess in guessed_number:
                print("⚠️ You already guessed that number.")
                continue

             guessed_number.append(guess)

             if guess in number:
                print("✅ Good guess!")
             else:
                attempt_left -= 1
                print(f"❌ Wrong! {attempt_left} tries left.")
        else:
           print("\n😢 You lost! The number was:", secret_code)
        play_again = input("do you want to play again?(Y/N)")
        if play_again.lower() == "n":
           print("ok, Bye!")
           break
        else:
           guessed_number = []
           print("\nnew game started!")
passwprd_guess()

         