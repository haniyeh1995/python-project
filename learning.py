# print("helo word")
# ----
# -variebale:
# int float str bool
# int:
# year = 1403
# print(year, type(year))
# folat:
# score = 19.75
# print (score,type(score))
# str:
# name = "Haniyeh"
# print (name,type(name))
# bool:
# is_done = False
# print(is_done,type(is_done))
# ---
# year, first_name, last_name, birth_date = (1400, 'haniyeh', 'nemati', '1995.09.07')
# print(year, first_name, last_name, birth_date)
# -----
# -interaction data with user:
# data_name = input("please enter your name : ")
# print(data_name)
# هر خروجی از اینپوت استرینگ است
# print(type (data_name))
# ------
# -convert of variebale:
# int() float() bool() str()
# type:str to int
# age = input("enter your age : ")
# print (age, type(age)) 
# int_age = int(age)
# print(type(int_age))
# year_birth =  1403 - int_age
# print(year_birth, type(year_birth))
# -----
# -operators + - / * // % **
# print (10 + 5)
# print (10 - 5)
# print (10 / 5)
# print (10 * 5)
# print (10 // 4) 
# ghesmate sahihe taqsim
# print (10 % 2) 
# baghimande taghsim
# print (10 ** 5)
#  tavan
# -------
# arithmentic operator:  += -= /= *= //= %= **=
# x = 10 
# x = x + 3
# print(x)
# with arithmentic:
# x = 10 
# x += 3
# x *= 2
# print(x)
# ------
# operator precedence --> ** * / % + - =
# x = 10 + 3 * 2
# print(x) ---->16
# ------
# comparison opearator ---> >= > < <= == !=
# x1 = 10
# x2 = 20
# print(x1 <= x2) ---->true or false
# ------
# logical operator ----> and-or- not(برعکس میکنه)
# age = 10
# print(age > 30 and age < 20)
# print(age > 30 or age < 20)
# print(not(age > 30 or age < 20))
# ------
#  strings
# first_name = "haniyeh"
# score = 29
# print("hello" + first_name + "your score is" + str(score))
# print("hello {first} your score is {score}".format(first = first_name , score = str(score)))
# print(f"hello {first_name} your score is {str(score)}")
# -------
# name = "haniyeh"
# print(name.upper())
# familly = "NEMATI"
# print(familly.lower())
# middle_name = "hana a"
# print(middle_name.capitalize())
# print(len(middle_name))       
# print(middle_name.count("a"))
# sentnce = "hello I love python"
# print(sentnce.find("python"))
# print(sentnce.replace("python" , "react"))
# or
# sentnce = sentnce.replace("python" , "react" )
# print(sentnce)
# print(sentnce.startswith('he'))
# the answer is true or false
# print(sentnce.endswith('react'))
# --------
# str to list
# sentnce = "hello I love python"
# print(type(sentnce.split()))
# print(sentnce[1])
# sentence22 = sentnce.split() 
# sentnce2 = "hello, I love python"
# print(sentnce2.split(','))
# -----
# sentnce = "hello I love python"
# print(sentnce.isalpha())
# sentnce2 = "helloIlovepython"
# print(sentnce2.isalpha())
# sentnce3 = "helloIlovepython"
# print(sentnce3.isalnum())
# sentnce4 = "33"
# print(sentnce4.isnumeric())
# -----
# list:
# student_name = ["haniyeh" , "ali" , "amir" , "reza"]
# family_name = list(("akbari", "asghari", "nemati" , "mohseni"))
# print(student_name, type(student_name))
# print(family_name, type(family_name))
# print(student_name[0])
# print(family_name[1])
# print(family_name[-1])
# print(family_name[-2])
# print(family_name[-3])
# print(len(student_name))
# student_name[1] = "sara"
# print(student_name)
# print(student_name[1:3])
# -----
# nums = [1,8,5,7]
# print(nums[1])
# nums.append(8)
# print(nums)
# nums.insert(1, 22)       insert(indexnum, X)
# print(nums)

# nums.remove(7)       remove(mohtava list)
# nums.pop(1)            pop(indexnum)
# print(nums)

# nums.reverse()
# print(nums)
# nums.sort()
# print(nums)
# print( 7 in nums)
# print( 20 in nums)
# the answer is true or false
# print(len(nums))
# nums.clear()
# print(nums)
# ------
# - tuple ----> لیستی که مقادیرش قابل تغییر نیست
# course = ("python" , "java", "react", "C++")
# print(len(course))
# print(course, type(course))
# tuple with one item
# course = ("python", )
# print(course, type(course))
# print(course[0])
# print(course[-1])
# del course
# print(course)
# course[1] = "html"
# print(course)     ----> Cannot
# ----------
# - Set ----> ایندکس ندارد/ مقدار تکراری قبول نمیکند ولی امکان اضافه یا کم کردن دارد
# course = {"python" , "java", "react", "C++"}
# print(course, type(course))
# course.add('cypress')
# print(course)
# course.add('java')
# print(course)
# course.remove('java')
# print(course)
# course.clear()
# print(course)
# --------
# - dictionary ----> دیتاهایی که از بک اند میاد  like obj in js
# student1 = {
#     "first_name" : "haniyeh",
#     "last_name" : "nematolahi",
#     "age": 29,
#     'is_femail': True,
# }


# print(student1, type(student1))
# del(student1['age'])
# print(student1)
# print(student1.get('first_name'))

# student2 = dict (first_name = "reza", last_name = "akbarii", age = 39, is_femail = False)
# print(student2, type(student2))

# print(student2.get('age'))
# print(student2['age'])

# student1['phone_number'] = '0912-8834543'
# print(student1)
# print(student1.keys())
# # print(student1.values())
# print(student1.items())

# person = student1.copy()
# person['city'] = 'tehran'
# print(person)
# del(person["city"])
# print(person)
# person.pop('age')
# print(person)
# print(len(person))
# person.clear()
# print(person)
# --
# - dict in list
# people = [
#     {"name" : "hani", "last_name": "nemati"},
#     {"name" : "reza", "last_name": "akbari"},
#     {"name" : "sara", "last_name": "ahmadi"}
# ]
# print(people, type(people))
# print(people[1]["name"])
# print(people[2]["last_name"])
# ----
# -functions
# def announcment (user):
#     print("Hello world")
#     x = user
#     print('Hello ' + x)

# announcment("user_agent")
# ---
# def name (firstname , lastname) :
#    full_name = firstname + lastname
#    print(full_name)
  
# name1 = input("please enter your name ")
# lastName2 = input("please enter your last name")
# name(name1 , lastName2)
# --------
# def announcmentt (user = "ali"):
#     x = user
#     print('Hello ' + x)

# announcmentt()
# ---
# def calculation(x,y):
#     sum = x + y
#     print(sum) 
    
# calculation(10,8)
# ---
# def calculation(x,y):
#     sum = x + y
#     return sum   
# result = calculation(10,8)
# print(result)
# ---
# def student_name(name):
#     y = name
#     print("my sudent name is " + y)

# student_name("zahra")
# ---
# def score(first,second):
#     moadel = (first + second)/2
#     print("your score is " + str(moadel))

# score(10,12)
# ---or
# def score(first,second):
#     moadel = (first + second)/2
#     return moadel

# final = score(10,12)
# print(final)
# ---
# Conditions:
# simple if:
# == , != , < , <= , > , >=
# 1.
# x = 30
# y = 20
# if x >= y :
#     print(f"{x} is greater than {y}")
# print("condition completed")
# 2.
# x = 40
# y = 46
# if x>y :
#     print('x is greater than y')
# else:
#     print(' y is greater')
# print("condition completed")
# 3.
# x = 40
# y = 40
# if x>y :
#     print('x is greater than y')
# elif x==y:
#     print (' x is equal to y')
# else:
#     print(' y is greater')
# 4.
# x = 40
# y = 40
# if x>y :
#     print('x is greater than y')
# elif x == 40:
#     print('x is 40')
# elif x==y:
#     print (' x is equal to y')
# else:
#     print(' y is greater')
# print("condition completed")
# اولین شرط درست را اجرا میکند و از حلقه خارج میشود
# ---
# nested if
# x = 30
# y = 20
# if x > y:
#     if x == 30:
#         print('x > y and is 30')
# print('done')
# هر دو شرط باید درست باشد تا پیام را چاپ کند
# ---
# logical operator
# and , or , not
# x = 30
# y = 20
# if x > y and x == 30:
#     print('x > y and is 30')
# print('done')
# x = 30
# y = 40
# if x > y or x == 30:
#     print('x > y and is 30')
# print('done')

# x = 10
# y = 20
# if not x == 30:
#     print('x is not 30')
# print('done')

# x = 10
# y = 20
# if not x < y:
#     print('x is not 30')
# print('done')
# ---
# membership(in, not in)
# num = [1,3,5,7,9]
# x= 3
# if x in num:
#     print('this number is in array')

# y = 11
# if y not in num:
#     print('this number is not in array')
# ---
# identity operator(is, is not)
# x = 30
# y = 30
# if x is y :
#     print('x is equal to y')

# x = 40
# y = 30 
# if x is not y:
#     print('x is not equal to y')
# ---
# loop: by for
# for i in range(5):
#     print(i)
# ----
# for i in range (1,7):
#     print(i)
# ----
# for index in range (0,10, 3):
#     print(index)
# -----
# sum = 0
# for num in range (6):
#     sum += num

# print(sum)

# 0
# 1
# 2
# 3
# 4
# 5

# 0+1 = 1
# 1+2= 3
# 3+3=6
# 6+4=10
# 10+5=15
# --------------------
# student = ["sara","sarvin","ali", "reza"]
# for item in student:
#     print(item)

# or

# for i in student:
#     if i == "ali":
#         break
#     print(f"current item : {i}")
# --------
# for i in range (len(student)):
#     print(i)
# ---------------
# while: It’ll execute the body as long as the condition is True infinity - so yo can made a condition

# while condition:
#     body

# max = 5
# counter = 0

# while counter < max :
#     print(counter)
#     counter += 1
# -----------------
# command= ""
# while command.lower() != "quit":
#       command = input('')
#       print(f"{command}")
# ------------------

# valid_years = list(range(1340, 1391))

# year_of_birth = None  

# while True:
#     year_of_birth = input("Enter your year of birth: ") 
#     year_of_birth = int(year_of_birth)
#     if year_of_birth not in valid_years:
#       print(f"Please enter a valid year of birth between {valid_years[0]} and {valid_years[-1]}.")
#       continue
#     age = 1403 - year_of_birth
#     if age > 30:
#       print(f"Your age is {age}. Unfortunately, we cannot hire applicants older than 30 years.")
#     else:
#       print(f"Your age is {age}. We can hire you!")
 
# -----------------------
# break
# for item in range (0, 5):
#       print(item)
#       if item == 2:
#         break
#       else:
#         print('the item is not valid')
# ---
# continue: The continue statement skips the current iteration and starts the next one.

# for i in range(10):
#     if i % 2 :
#         continue
#     print(i)
# ----------
# module:

# from camelcase import CamelCase
# c = CamelCase()
# print(c.hump("this is python course"))
# -------------
# import external module:

# from validateEmail import validate_email
# email = input("")
# print(validate_email(email))
# -----examples:
# fac = 1

# for i in range (1,6):
#  fac = fac * i

# print (fac)
# ------
# for i in "hello":
#     print (i)
# -----
# x = 8
# fib = [0, 1]
# for i in range (2, x):
#   fib.append(fib[i - 1] + fib [i - 2])
# print(fib)
# -----------
# n = 5
# for i in range(1, n): 

#     print('*' * i)
# -------
# n = 4
# for i in range(n ,0, -1): 
#     print('*' * i)
# ---------
# For all non-negative integers i < n . print i **2

# n = 4

# for i in range (0 , n):
#     print(i ** 2)
# ------
# for i in range (1,3):
#     for j in range(1,7):
#         print (j)

# -----
# for i in range (1,4):  
#     for j in range (1,6):  
#         print("*", end=" ")
#     print()
# _______

# for i in range (1,4):
#     for j in range (1 , i+1):
#         print("*", end = " ")
#     print()
   
# ----------
# for i in range (3,0, -1):
#     for j in range (i, 0 , -1):
#         print("*", end = " ")
#     print()

# ------------

# تبدیل دیکشنری به جیسون برای انتقال داده ها به بکند

# import json

# student = {
#     "first_name" : "haniyeh",
#     "last_name" : "nematolahi",
#     "age": 29,
#     'is_femail': True,
# }

# student_json = json.dumps(student)
# print(student_json)
# # ------reverse
# sampleJson = '{"name": "zahra" , "age" : 29 , "gender" : "female"}'
# sampleToDic = json.loads(sampleJson)
# print(sampleToDic)
# --------------------------------------------------------------
# closure

# def parent_function(player):
#     coins = 5

#     def play_game():
#         nonlocal coins
#         coins -= 1
#         print(f"{player} has {coins} coins left")

#     return play_game

# user1 = parent_function("hani")
# user1()
# user1()

# user2 = parent_function("ebi")
# user2()
# user2()

# user1()
# -----------------------------------------

# def make_counter():
#     count = 0

#     def counter():
#         nonlocal count
#         count += 1
#         return count
#     return counter

# counter1 = make_counter()
# print(counter1())
# print(counter1())
# print(counter1())
# print(counter1())

# counter2 = make_counter()
# print(counter2())
# print(counter2())
# ---------------------------------

# def make_multiplier(factor):

#     def multipliction(number):
#         result = number * factor
#         return result
#     return multipliction


# times1 = make_multiplier(3)
# print(times1(10)) 

# times2 = make_multiplier(5)
# print(times2(20))
# ---------------------------------------
# import time

# def make_otp_generator(seed):
    
#     def generate_otp():
#         now = int(time.time())
#         otp = (seed * now) % 1000000 
#         return str(otp).zfill(6)
#     return generate_otp

# otp_gen = make_otp_generator(123456)
# print("otp1:" , otp_gen())

# ----------------------------------------
# class:

# class AnimalINTown:
#     def __init__(self, name = "unknown", age, sex):  #constructor
#         self.name = name
#         self.age = age
#         self.gender = sex

#     def information(self):
#         print(f"{self.name} is {self.age} years old and it is {self.gender}") 

#     def eating_things(self):
#         print(f"{self.name} eats meat and vegtable")

#     def behavior(self):
#         print("smooth and good")

    
# third_sample = AnimalINTown("fandogh", 2, "boy")
# third_sample.information()
# print(third_sample.gender)

# first_sample = AnimalINTown("tedy", 9, "girl")
# first_sample.eating_things()
# print(first_sample.age)

# second_sample = AnimalINTown()
# second_sample.behavior()
# ------------------------------------------------------------------------

# import threading
# import time

# def print_numbers():
#     for i in range(5):
#         print(f"Numbers: {i}")
#         time.sleep(1) 

# def print_letters():
#     for letter in "ABCDE":
#         print(f"Letters: {letter}")
#         time.sleep(1)

# t1 = threading.Thread(target=print_numbers)
# t2 = threading.Thread(target=print_letters)

# t1.start()
# t2.start()

# t1.join()
# t2.join()

# print("all threads done")
# -----------------------------------------------
# import requests


# response = requests.get("https://api.github.com")

# print("Status code:", response.status_code)


# print("Response text:", response.text)

# ----------------------------------------------
# import threading
# import requests
# import time


# urls = [
#     "https://aparat.com",
#     "https://youtube.com/delay/2", 
#     "https://www.python.org"
# ]

# def download_site(url):
#     print(f"شروع دانلود: {url}")
#     response = requests.get(url)
#     print(f"دانلود کامل شد {len(response.content)}{url}")

# start_time = time.time()
# threads = []


# for url in urls:
#     thread = threading.Thread(target=download_site, args=(url,))
#     threads.append(thread)
#     thread.start()


# for thread in threads:
#     thread.join()

# end_time = time.time()
# print(f"زمان کل: {end_time - start_time:.2f} ثانیه")
# ----------------------------------------------------------------------
# import threading

# def hello(name, delay):
#     print(f"hi {name}! after {delay} second")

# t = threading.Thread(target=hello, args=("haniyeh", 3))
# t.start()
# ------------------------------------------------