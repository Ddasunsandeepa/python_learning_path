# print("hello world")

# #strings

# first_name = "dasun"
# print(first_name)

# #f-string - for format variables with string literals

# print(f"hello {first_name}")
# print("hello" + " " + first_name)

# #integers

# age = 25
# quantity = 3

# print(f"your age is {age} years old")
# print(f"i buy {quantity} items.")

# #float

# price = 3.25
# age= 25
# print(f"your age is {age} years old")
# print(f"the price of the item is {price}")

# print(f"that item cost is ${price}")

# #boolean

# is_student = True

# print(f"is he a student? {is_student}")
# if(is_student) :
#   print("hello")
# else :
#   print("bye")

# #typecasting   str()  int()  bool()  float()

# name = "dasun"
# age = 22
# gpa = 3.8
# is_student = True

# print(type(name))
# print(type(age))
# print(type(gpa))
# print(type(is_student))

# age = float(age)
# print(age)

# gpa = int(gpa)
# print(gpa)

# is_student = str(is_student)
# print(is_student)
# print(type(is_student))

# age = bool(age)
# print(age)

# print(bool(gpa))
# print(bool(name))
# print(bool(is_student))
# print(bool(gpa))

# input1 = "22"
# print(type(input1))
# print(type(input1))

# x =1
# y = 1
# print(x == y)

# if x == y :
#   print("x is equal to y")
# else :
#   print("x is not equal to y")

# print("hello")
# x=20
# print(x)
# x = 20
# print(x)

# gpa = 3.8
# gpa = str(gpa)
# print(gpa)
# print(type(gpa))
# print(f"my gpa is {gpa}")

# age = 0
# age = bool(age)
# print(age)
# print(type(age))

# das = input("enter your name : ")
# print(f"hello {das}")

# age = input("enter your age : ")
# age = int(age)
# age +=1
# print(f"your age is {age}")
# print(type(age))

# #are of a rectangle

# length = float(input("enter the length of the rectangle : "))
# width = float(input("enter the width of the rectangle : "))

# area = int(length*width)
# print(f"the area of the rectangle is {area}cm²")

# # Madlibs game
# # Word game where you create a story
# # by filling in blanks with random words

# adjective1 = input("Enter an adjective (description): ")
# noun1 = input("Enter a noun (person, place, thing): ")
# adjective2 = input("Enter an adjective (description): ")
# verb1 = input("Enter a verb ending with 'ing': ")
# adjective3 = input("Enter an adjective (description): ")

# print(f"Today I went to a {adjective1} zoo.")
# print(f"In an exhibit, I saw a {noun1}.")
# print(f"{noun1} was {adjective2} and {verb1}.")

 

# test = " "
# test = bool(test)
# print(test)

# num1 = float(input("enter the first number : "))
# num2 = float(input("enter the second number : "))
# operator = input("enter the operator(+,-,/,*,**,%) : ")

# if operator == "+":
#     result = num1 + num2
# elif operator == "-":
#     result = num1 - num2
# elif operator == "*":
#     result = num1 * num2
# elif operator == "/":
#     result = num1 / num2
# elif operator == "**":
#     result = num1 ** num2
# elif operator == "%":
#     result = num1 % num2
# else:
#     print("invalid operator")
#     result = None

# if result == None:
#     print("result is None")
# else:
#     print(f"the result is {round(result, 2)}")


s = int(input("enter a number : "))
print(f"the number is {s}")

name = input("enter your name : ")

if len(name) > 12:
    print("name is too long.. need to be less than 12 characters")
elif name.find(" ") != -1:
    print("name should not contain spaces")
elif name.isdigit() == False:
    print("name should not contain digits")
else:
    print(f"name is valid.. hello {name}")

print("hello world {(4+8)}")

v = 10
g =12

print(f"hello {v} and {g} and sum is {v+g}")
print(f"hello {4+3}")

food = input("enter your fav food or q for quite :")

while not food == "q" :
    if food == "":
        print("food cannot be empty")
    else :
        print(f"your fav food is {food}")

    food = input("enter your fav food or q for quite :")
print("thank you for using the program")

my_list = [1,2,3,"e"]
print(my_list)