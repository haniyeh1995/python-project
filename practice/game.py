# scissors /paper /stone game

import random
import sys

# while True:
#     option_user1 = input("\nplease choose your option user1:\nscissors = 1\npaper = 2\nstone = 3 \n(or type 'exit' to quit)\n\n")

#     if option_user1.lower() == "exit":
#        print("bye")
#        break
#     if option_user1.isdigit():
#       option_user1 = int(option_user1)
#       if option_user1 not in [1,2,3]:
#         print("You must enter a digit between 1 and 3.")
#         sys.exit()  
#       option_user2 = random.randint(1,3)
#       print(f"Your choice is {option_user1} and computer choice is {option_user2}")

#       if option_user1 == 1 and option_user2 == 2:
#          print("you win")
#       elif option_user1 == 2 and option_user2 == 3:
#          print("you win")
#       elif option_user1 == 3 and option_user2 == 1:
#          print("you win")
#       elif option_user1 == option_user2:
#          print ("equal")
#       else:
#          print("computer win")
#     else:
#        print("Enter a valid number")
     
# or

def game():
    option_user1 = input("\nplease choose your option user1:\nscissors = 1\npaper = 2\nstone = 3 \n(or type 'exit' to quit)\n\n")

    if option_user1.lower() == "exit":
       print("bye")
       return
    if option_user1.isdigit():
      option_user1 = int(option_user1)
      if option_user1 not in [1,2,3]:
        print("You must enter a digit between 1 and 3.")
        sys.exit()  
      option_user2 = random.randint(1,3)
      print(f"Your choice is {option_user1} and computer choice is {option_user2}")

      if option_user1 == 1 and option_user2 == 2:
         print("you win")
      elif option_user1 == 2 and option_user2 == 3:
         print("you win")
      elif option_user1 == 3 and option_user2 == 1:
         print("you win")
      elif option_user1 == option_user2:
         print ("equal")
      else:
         print("computer win")
      
      return game()
    
    else:
       print("Enter a valid number")
game()   


