# Choose Even or Odd: even
# Enter your number (between 1 to 5): 2
# Computer chose: 3
# Total is 5 → It's odd!
# You chose: even
# Computer wins!

import random

def even_or_odd ():
    
    while True:
        Even_Odd = input("Choose even or odd:\n").lower()
        if Even_Odd.isalpha():
         user_number = int(input("Enter your number (between 1 to 5):\n"))
         if user_number % 2 == 0 :
            print(f"your number is {user_number} and it is Even")
         else:
            print(f"your number is {user_number} and it is Odd")
        
         computer_number = random.randint(1,5)
         print(f"computer number is {computer_number}")

         Total = user_number + computer_number
         print(f"Total is {Total}")

         if Total % 2 == 0 :
            result = "even"
            print("it is Even")
         else:
            result = "odd"
            print("it is Odd")

         if Even_Odd == result:
            print("you win")
         else:
            print("computer win")

         play_again = input("Do you want to play again? (yes/no): \n").lower()
         if play_again == "no":
            print("goodbye!")
            break
         else:
            continue
        else:
           print("please enter even or odd")

even_or_odd()

