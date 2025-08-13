# password = "1674"

# for count in range(3):
#     user_password = input("please enter your password:")
#     if user_password == password :
#         print("correct password")
#         break   
#     else:
#         print('your password is wrong')
# else:
#     print('end of opportunity')

# ----------------------------
# def user_neum (num):
#     total = num + 1
#     print(total)

# user_neum(10)

# ----------------
# def user_neum (num):
#     if num >= 5:
#         return num    
#     total = num + 1
#     print(total)
#     return user_neum(total)

# user_neum(2)

# ---------------------
# calculate(4, 2, '+') → 6  
# calculate(5, 3, '*') → 15  
# calculate(10, 2, '/') → 5.0

# def calculate (num1,num2):
#     result = num1 + num2
#     print(result)

# calculate(4,2)

# def calculate2 (num1,num2):
#     result = num1 * num2
#     print(result)

# calculate2(5,3)

# def calculate3 (num1,num2):
#     result = num1 / num2
#     print(round(result))

# calculate3(10,2)

# merge to 1 function:

# def calculation (num1,num2,operator):
#     if operator == "+" :
#         return num1 + num2
#     elif operator == "*":
#         return num1 * num2 
#     elif operator == "/":
#         return num1 / num2
#     else:
#         print("operater did not defined")

# print(calculation(4,2, "+"))
# print(calculation(5,3, "*"))
# print(calculation(10,2, "/"))
# print(calculation(1,2, "-"))

# ----------------------------
# is_palindrome("madam") → True  
# is_palindrome("hello") → False

# word = "hello"
# array_word = word.split()
# print(type(array_word))
# print(word[1])
# print(word[::-1])

# def is_palindrome (word):
#     if word == word[::-1]:
#         print('the word is palimdrome') 
#     else:
#         print('the word is not palimdrome') 
    
# is_palindrome("hello")
# is_palindrome("madam")

# or

# def palindrome (word):
#     return word == word[::-1]

# print(palindrome("hello"))
# print(palindrome("madam"))
# -----------------------------------
# find_max = [1, 5, 3, 9, 2] 
# print(max(find_max))
# # or
# sorted_list = sorted(find_max)
# print(sorted_list[-1])


# def find_max(numbers):
#     max_num = numbers[0]
    
#     for num in numbers[1:]:
#         if num > max_num:
#             max_num = num  
    
#     return max_num

# print(find_max([1, 5, 3, 9, 2]))
# -------------------------------------
# count_vowels("hello world") → 3

# def find_vowels (letter):
#     vowels = ["a", "e" , "o" , "i" , "u", "O", "A" , "E" , "I", "U"]
#     total = []

#     for x in letter:
#         if x in vowels :
#             total.append(x)

#     return total

# print(find_vowels("I have some Eggs"))
# ----------------------------------------------

# def count_vowels (word):
#     vowels = "aeiouAEIOU"
#     count = 0

#     for char in word:
#         if char in vowels:
#             count += 1
#     return count

# print(count_vowels("hello world And HI"))

# ----------------------------------------------------
# Write a function greet_user(name, is_morning) that prints:

#     "Good morning, [name]!" if is_morning is True

#     "Hello, [name]!" if is_morning is False


# def greet_user(name, is_morning):
#     if is_morning == True :
#         print(f"Good morning, {name}!")
#     else:
#         print (f"Hello, {name}!")


# greet_user("haniyeh", True)
# greet_user("haniyeh", False)
# -------------------------------------

# import random
# import platform
# import os

# num = random.randint(1,10)
# user_guess = int(input("please guess the number from 1 to 10 : \n"))

# if user_guess == num:
#     print("wonderful! you guess correctly")
# else:
#     if platform.system() == "Windows":
#         os.startfile(r"C:\Users\Hanieh\Desktop\image.jpg")

# print(f"computer number is: {num}")
# -------------------------------------------------
# count_even_odd([1, 2, 3, 4, 5, 6])  # → {'even': 3, 'odd': 3}

# def count_even_odd(numbers):
#     even_count = 0
#     odd_count = 0 
#     for x in numbers:
#         if x % 2 == 0:
#             even_count +=1
#         else:
#             odd_count +=1
#     return {'even': even_count, 'odd': odd_count}


# print(count_even_odd([1, 2, 3, 4, 5, 6, 50]))

# ---------------------------------------------------------
# reverse_words("hello world")  # → "olleh dlrow"
# x = "hello world"
# words = x.split()
# print(words)


# def reverse_words (sentence):
#     words = sentence.split()
#     reversed_list = []

#     for x in words:
#         reversed_list.append(x[::-1])

#     return ' '.join(reversed_list)


# print(reverse_words("hello world"))
 
# ----------------------------------------------------- 
# multiply_all

# def multiply_all(numbers):
#     result = 1
#     for i in numbers:
#         result *= i
               
#     return result

# print(multiply_all([1, 2, 3, 4, 10])) 
# ----------------------------------------

# prime_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]


# def is_prime(n):
#     if n <= 1:
#         return False

#     for i in range(2, int(n**0.5) + 1):  # Only check up to square root of n
#         if n % i == 0:
#             return False

#     return True


# print(is_prime(2))        
# print(is_prime(4))    
# print(is_prime(13))   
# print(is_prime(1))    
# -----------------------------------------

# def longest_word(words):
#     langest = ''

#     for i in words:
#         if len(i) > len(langest):
#             langest = i
#     return langest


# print(longest_word(["cat", "elephant", "tiger"]))
# -----------------------------------------------------

# def remove_vowels(text):
#     vowels = "aeouiAEOUI"
#     result = ""

#     for i in text:
#         if i not in vowels:
#             result += i
#     return result
            

# print(remove_vowels("Hello World"))  
# -----------------------------------

# def count_words(sentence):
#     word = sentence.split()
#     count = 0

#     for i in word:
#         count += 1 
#     return count

# print(count_words("Python is fun, to learn, and easy"))

# or

# def count_words(sentence):
#     word = sentence.split()
    
#     return len(word)

# print(count_words("Python is fun to learn"))

# ---------------------------------------------------------

# def fizz_buzz(n):
#     if n % 3 == 0 and n % 5 == 0 :
#         print("FizzBuzz")
#     elif n %  3 == 0 :
#         print("Fizz")
#     elif n % 5 == 0 :
#         print("Buzz")
#     else:
#         print(n)
        
# while True:
#     user_input = input("Write your number (or type 'exit' to quit):\n")
    
#     if user_input.lower() == "exit":
#         print("Goodbye!")
#         break

#     if user_input.isdigit():
#         number = int(user_input)
#         fizz_buzz(number)
#     else:
#         print("Please enter a valid number.")
# --------------------------------------
# def capitalize_words(text):
#     words = text.split()
#     capitalize_word = []

#     for word in words:
#         capitalize_word.append(word.capitalize())

#     return " ".join(capitalize_word)


# print(capitalize_words("i love pythone too much"))

# -------------------------------------------------
# def common_elements(list1,list2):
#     common_list = []

#     for item in list1:
#         if item in list2 and item not in common_list:
#          common_list.append(item)
#     return common_list


# print(common_elements([1, 2, 3, 2],[2, 3, 4]))  

# or

# def common_elements(list1, list2):
#     return list(set(list1) & set(list2))
# print(common_elements([1, 2, 3],[2, 3, 4]))  
# ------------------------------------------------------------
# def count_digits(n):
#     count = 0

#     for i in n:
#         if i.isdigit():
#             count += 1
#     return count 

# print(count_digits("1234578fhj"))  
# ----------------------------------------------------------
# def reverse_sentence(sentence):
#     words = sentence.split()
#     reversed = words[::-1]

#     return " ".join(reversed)

    
# print(reverse_sentence("hi I love Python"))  
# ----------------------------------------------------------
# def remove_duplicates(lst):
#     removed_list = []

#     for i in lst:
#         if i not in removed_list:
#             removed_list.append(i)
#     return removed_list

# print(remove_duplicates([1, 2, 2, 3, 1, 4]))  
# ------------------------------------------------------------
# def first_last_same(numberList):
#     print("Given list:", numberList)
#     first_num = numberList[0]
#     last_num = numberList[-1]

#     if first_num == last_num:
#         return True
#     else:
#         return False
 
# numbers_x = [10, 20, 30, 40, 10]
# print("result is", first_last_same(numbers_x))
 
# numbers_y = [75, 65, 35, 75, 30]
# print("result is", first_last_same(numbers_y)) 
# ----------------------------------------------------------

# class

# user_name = input("please enter your name: \n")
# enterance_money = float(input("please enter your initial balance: \n"))

# class BankAccount :
#     def __init__(self, owner, balance = 0 ):
#         self.owner = owner
#         self.balance = balance
    
#     def deposit(self, amount):
#         self.balance += amount
#         print(f"Thanks {self.owner}, your balance is: {self.balance}")
    
#     def withdraw(self, amount):
#         if self.balance >= amount :
#            self.balance -= amount
#            print(f"{self.owner}, your balance is: {self.balance}")
#         else:
#             print(f"{self.owner}, your balance is not enough")

#     def display_balance(self):
#         print(f"your final balance is {self.balance:.2f}")

# user_account = BankAccount(user_name, enterance_money)

# deposit_amount = float(input("How much would you like to deposit? \n"))
# user_account.deposit(deposit_amount)

# withdraw_amount = float(input("How much would you like to withdraw? \n"))
# user_account.withdraw(withdraw_amount)

# user_account.display_balance()
# ------------------------------------------------------------
# class 2

# book_title = input("Enter your book'name: \n")
# book_author = input("Enter your book'author: \n")
# book_total_pages = int(input("Enter your book'total_pages: \n"))

# class Book:
#     def __init__(self, title, author, total_pages, current_page = 1):
#         self.title = title
#         self.author = author
#         self.total_pages = total_pages
#         self.current_page = current_page
    
#     def read(self, pages): 
#         if self.current_page + pages >= self.total_pages:
#            self.current_page = self.total_pages
#            print(f"you've already finish the book! the book has {self.current_page} pages")
#         else:
#             self.current_page += pages
#             print(f"you are at page {self.current_page}")
    
#     def bookmark(self):
#         print(f"you are at page {self.current_page} right now")
    
#     def page_remaining(self):
#         remain = self.total_pages - self.current_page 
#         print(f"{remain} pages of your book remains")

#     def book_info(self):
#         print(f"You are currently reading '{self.title}' by {self.author}. Page {self.current_page}/{self.total_pages}")


# my_book = Book(book_title, book_author, book_total_pages)
# read_pages = int(input("how many pages of your book do you read now? \n"))
# my_book.read(read_pages)
# my_book.bookmark()
# my_book.page_remaining()
# my_book.book_info()

# --------------------------------------------------
 
# class Movie:
#     def __init__(self, title, director, duration, watched_minute = 0):
#         self.title = title
#         self.director = director
#         self.duration = duration
#         self.watched_minute = watched_minute

#     def watch(self, minute):
#         if self.watched_minute + minute >= self.duration:
#             self.watched_minute = self.duration
#             print(f"You've finished watching '{self.title}'")
#         else:
#             self.watched_minute += minute
#             print(f"you watch {self.watched_minute} minute of the '{self.title}'")
    
#     def movie_info(self):
#         print(f"you are watching {self.title} by {self.director} and the duration of movie is {self.duration} minute")
    
#     def remaining_time(self):
#         remain = self.duration - self.watched_minute
#         print(f"{remain} miunte of movie is remaining")


# my_movie = Movie("insidious","Gorge Dc", 190)
# my_movie.watch(100)
# my_movie.watch(100)
# my_movie.watch(90)
# my_movie.movie_info()
# my_movie.remaining_time()

# movies = [
#     Movie("Inception", "Christopher Nolan", 148),
#     Movie("Interstellar", "Christopher Nolan", 169),
#     Movie("Avatar", "James Cameron", 162)
# ]

# for i in movies:
#     i.movie_info()
#     watch_time = int(input(f"How many minutes of '{i.title}' did you watch? "))
#     i.watch(watch_time)
#     i.remaining_time()
# -----------------------------------------------------------------------
# class Movie:
#     def __init__(self, title, director, duration, watched_minute = 0):
#         self.title = title
#         self.director = director
#         self.duration = duration
#         self.watched_minute = watched_minute

#     def watch(self, minute):
#         if self.watched_minute + minute >= self.duration:
#             self.watched_minute = self.duration
#             print(f"You've finished watching '{self.title}'")
#         else:
#             self.watched_minute += minute
#             print(f"you watch {self.watched_minute} minute of the '{self.title}'")
    
#     def movie_info(self):
#         print(f"🎬{self.title} | Director: {self.director} | Duration: {self.duration} minute | Watched: {self.watched_minute}")
    
#     def remaining_time(self):
#         return self.duration - self.watched_minute
    
# movies = []

# while True:
#     print("\n🎞 Movie Manager Menu:")
#     print("1. Add movie")
#     print("2. Delete movie")
#     print("3. Watch movie")
#     print("4. Show movie list")
#     print("5. Show remaining time")
#     print("6. Exit")        


#     choice = int(input("enter your option from 1 to 6: \n"))

#     if choice == 1 :
#         title = input("Enter movie title: ")
#         director = input("Enter director name: ")
#         duration = int(input("Enter duration (in minutes): "))
#         movies.append(Movie(title, director, duration))
#         print(f"✅ Movie '{title}' added.")

#     elif choice == 2 :
#          for idx, m in enumerate(movies):
#             print(f"{idx + 1}. {m.title}")
#          delete_index = int(input("Enter movie number to delete: ")) - 1
#          if 0 <= delete_index < len(movies):
#             removed = movies.pop(delete_index)
#             print(f"🗑 '{removed.title}' deleted.")
#          else:
#             print("❌ Invalid number.")

#     elif choice== 3 :
#         for idx, m in enumerate(movies):
#             print(f"{idx + 1}. {m.title}")
#         index = int(input("Which movie did you watch? ")) - 1
#         if 0 <= index < len(movies):
#             minutes = int(input("How many minutes did you watch? "))
#             movies[index].watch(minutes)
#         else:
#             print("❌ Invalid number.")
    
#     elif choice == 4 :
#         if movies:
#             print("\n📚 Your Movies:")
#             for m in movies:
#                 m.movie_info()
#         else:
#             print("⚠️ Movie list is empty.")

#     elif choice == 5:
#         for m in movies:
#             print(f"{m.title}: {m.remaining_time()} minutes remaining.")

#     elif choice == 6:
#         print("👋 Exiting Movie Manager. Goodbye!")
#         break

#     else:
#         print("❌Invalid choice. Please select 1 to 6.")

# ----------------------------------------------------------------------------
# import json
# import os

# class Product:
#     def __init__(self, name, price, quantity = 0):
#         self.name = name
#         self.price = price
#         self.quantity = quantity
    
#     def update_stock(self, amount):
#         self.quantity += amount
#         print(f"the quantity of {self.name} updatetd. New quantity: {self.quantity}")
    
#     def purchase(self, amount):
#         if self.quantity >= amount :
#             self.quantity -= amount
#             total_price = self.price * amount
#             print(f"🛒 You bought {amount} of {self.name}. Total price: {total_price} Toman")
#         else:
#             print(f"Not enough stock!")
    
#     def product_info(self):
#         print(f"📌 {self.name} | Price: {self.price} Toman | In stock: {self.quantity}")

#     def to_dict(self):
#         return {
#             "name" : self.name ,
#             "price": self.price ,
#             "quantity" : self.quantity
#         }
    
#     @classmethod
#     def from_dict(clss, data):
#         return clss(data["name"], data["price"], data["quantity"])
    

# # --------------------------saving methods--------------------------------

# def save_products(products, filename="store.json"):
#     data = [p.to_dict() for p in products]
#     with open(filename, "w") as f:
#         json.dump(data, f)

# def load_products(filename="store.json"):
#     if not os.path.exists(filename):
#         return []
#     with open(filename, "r") as f:
#         data = json.load(f)
#         return [Product.from_dict(p) for p in data]

# # ---------------------------main program------------------------------------
# products = load_products()
# print("📦 Products loaded from file.")

# while True:
#     print("\n🛍 Store Menu:")
#     print("1. Add Product")
#     print("2. Update Stock")
#     print("3. Purchase Product")
#     print("4. Show All Products")
#     print("5. Exit\n")

#     try:
#         choice = int(input("Choose an option (1-5): "))
#     except ValueError:
#         print("⚠️ Please enter a number.")
#         continue

#     if choice == 1:
#         name = input("type your product name: \n")
#         price = int(input("type it's price in Toman: \n"))
#         quantity = int(input("type the quantity: \n"))
#         products.append(Product(name, price, quantity))
#         save_products(products)
#         print(f"\n'{name}' added to inventory.")
        

#     elif choice == 2:
#         for idx , m in enumerate(products):
#             print(f"{idx + 1}. {m.name}")
#         index= int(input("which product to update? \n")) - 1
#         if  0 <= index < len(products):
#             amount = int(input("how many units to add? \n"))
#             products[index].update_stock(amount)
#         else:
#             print("❌invalid selection")
#         save_products(products)
    
#     elif choice == 3:
#         for idx , m in enumerate(products):
#             print(f"{idx + 1}. {m.name}")
#         index = int(input("which product to buy? \n")) - 1
#         amount = int(input("how many units to buy? \n"))
#         if  0 <= index < len(products):
#             products[index].purchase(amount)
#         else:
#             print("❌invalid selection")
#         save_products(products)
    
#     elif choice == 4:
#         if products:
#             print("\n📦Product List:")
#             for m in products:
#                 m.product_info()
#         else:
#             print("📭No products available.")
        
#     elif choice == 5:
#         print("👋 Exiting Store Menu. Goodbye!")
#         break
    
#     else:
#         print("❌Invalid choice. Please select 1 to 6.")
# -----------------------------------------------------------------------

    





    

    