print("hello world")

#strings

first_name = "dasun"
print(first_name)

#f-string - for format variables with string literals

print(f"hello {first_name}")
print("hello" + " " + first_name)

#integers

age = 25
quantity = 3

print(f"your age is {age} years old")
print(f"i buy {quantity} items.")

#float

price = 3.25

print(f"that item cost is ${price}")

#boolean

is_student = True

print(f"is he a student? {is_student}")
if(is_student) :
  print("hello")
else :
  print("bye")

#typecasting   str()  int()  bool()  float()

name = "dasun"
age = 22
gpa = 3.8
is_student = True

print(type(name))
print(type(age))
print(type(gpa))
print(type(is_student))

age = float(age)
print(age)

gpa = int(gpa)
print(gpa)

is_student = str(is_student)
print(is_student)
print(type(is_student))

age = bool(age)
print(age)

print(bool(gpa))
print(bool(name))
print(bool(is_student))
print(bool(gpa))

input1 = "22"
print(type(input1))
print(type(input1))

x =1
y = 1
print(x == y)

if x == y :
  print("x is equal to y")
else :
  print("x is not equal to y")

print("hello")
x=20
print(x)
x = 20
print(x)

gpa = 3.8
gpa = str(gpa)
print(gpa)
print(type(gpa))
print(f"my gpa is {gpa}")

age = 0
age = bool(age)
print(age)
print(type(age))

das = input("enter your name : ")
print(f"hello {das}")

age = input("enter your age : ")
age = int(age)
age +=1
print(f"your age is {age}")
print(type(age))