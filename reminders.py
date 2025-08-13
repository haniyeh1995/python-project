# user_name = input("please type your name:\n") 
# user_age = input("please type your age:\n") 
# user_city = input("which city do you live?\n") 

# if user_age.isdigit():
#     print(f"Hello {user_name.capitalize()}, you are {user_age} and live in {user_city.capitalize()}.")
# else:
#     print("you must enter a number for your age")
# ----------------------------------------
# name = input("please enter your name: ")

# while True:
#     age = input("please enter your age: ")
    
#     if age.isdigit():
#         age = int(age)
#         city = input("please enter your city name: ")  
        
#         if age < 18:      
#             print("hello young", name, age, city)
#         else:
#             print("hello", name, age, city)
#         break  
#     else:
#         print("You must enter a number for your age. Try again.")

# -----------------------

# user_number = int(input("type your number:\n"))

# if user_number == 0 :
#     print("zero is neither Even nor Odd")
# elif user_number % 2 == 0 :
#     print("your number is Even ")
# else:
#     print("your number is Odd")

# ------------------------------

# user_nums = input("type 3 number and seperated them by space:\n")
# numbers = user_nums.split()

# total = 0
# for i in numbers:
#     total += int(i)
    
# print("Sum:" , total)

# --------------------------------------

# user_num = int(input("type your number:\n"))

# for nums in range (1,11):
#     print(f"{user_num} * {nums} = {user_num * nums}")
# -------------------------------------------------------------
# def is_prime(n):
#     if n <= 1:
#         return False  
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False  # اگر بخش‌پذیر بود، اول نیست
#     return True


# num = int(input("Enter a number to check if it's prime: "))

# if is_prime(num):
#     print(f"{num} is a prime number.")
# else:
#     print(f"{num} is NOT a prime number.")
# ------------------------------------------------------------
# def vowel_sound(letter):
#     vowel_letter = "aeuioAEUIO"

#     count = 0
#     for i in letter:
#       if i in vowel_letter:
#         count += 1
#     return count

# user_sentence = input("Enter your sentences:\n")

# print(vowel_sound(user_sentence))
# ------------------------------------------------

# import random

# while True:
#     computer_num = random.randint(1,10)
#     user_guess = int(input("please guess the number from 1 to 10 : \n"))

#     if user_guess == computer_num :
#        print("You guess right!")
#        break
#     else:
#        print(f"Wrong guess. Try again, computer number was {computer_num}")
      
      
# ------------------------------------------------------------------------------------------

# print(len(user_password))

# while True:
#     user_password = input("Enter your password: \n")

#     if len(user_password) < 8 :
#         print("please choose a strong password")
#     else:
#         print("Strong password!")
#         break
        
# -----------------------------------------------------

# def power(a,b):
#    result = a ** b
#    print(result)

# first_number = int(input("enter your first number: \n"))
# second_number = int(input("enter your second number: \n"))
# power(first_number, second_number)
# -------------------------------------------------------------
# 5 = 5 * 4 * 3 * 2 * 1 = 120
# def factorial(n):
#     result = 1
#     for i in range(1, n+1):
#         result *= i
#     return result
    
        
# user_number = int(input("Enter your number: \n"))
# print(factorial(user_number))

# --------------------------------------------------
