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

#typecasting

name = "dasun"
age = 22
gpa = 3.8
is_student = True

print(type(name))
print(type(age))
print(type(gpa))
print(type(is_student))