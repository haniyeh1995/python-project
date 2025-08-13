# Enter first number: 10
# Enter second number: 5
# Choose operation (+, -, *, /): *
# Result: 50


def calculation():
    while True:
     try:
      first_number = int(input("Enter your first number:\n"))
      second_number = int(input("Enter your second number:\n"))
     except ValueError:
         print("Enter a number") 
         continue

     operator = input("Choose operation (+, -, *, /):\n")

     if operator == "+":
        result = first_number + second_number
     elif operator == "-":
        result = first_number - second_number
     elif operator == "*":
        result = first_number * second_number
     elif operator == "/":
        if second_number == 0:
           print("Can not devided by zero")
           continue
        result = first_number / second_number
     else:
        print("invalid operator")
        continue
     print(f"Result: {result}")

     play_again= input("Do you want to play again?(yes/no):\n")
     if play_again.lower() == "no":
        print("ok, Bye!")
        break
     else:
        continue 
calculation()
