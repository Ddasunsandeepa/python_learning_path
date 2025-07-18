principle = 0
time = 0
rate = 0

while True:
    user_input = input("Enter the principle amount: ")
    if user_input.strip() == "":
        print(" Principle cannot be empty.")
        continue
    try:
        principle = float(user_input)
        if principle < 0:
            print(" Principle cannot be negative.")
        else:
            break
    except ValueError:
        print(" Invalid number.")

while True:
    user_input = input("Enter the time: ")
    if user_input.strip() == "":
        print(" Time cannot be empty.")
        continue
    try:
        time = float(user_input)
        if time < 0:
            print(" Time cannot be negative.")
        else:
            break
    except ValueError:
        print(" Invalid number.")

while True:
    user_input = input("Enter the rate: ")
    if user_input.strip() == "":
        print(" Rate cannot be empty.")
        continue
    try:
        rate = float(user_input)
        if rate < 0:
            print(" Rate cannot be negative.")
        else:
            break
    except ValueError:
        print(" Invalid number.")

result = principle * (1 + (rate / 100) * time)
print(f"\n The compound interest for {time} years is: ${result:.2f}")

while True:
    user_input = input("Enter the time: ")
    if user_input.strip() == "":
        print(" Time cannot be empty.")
        continue
    try:
        time = float(user_input)
        if time < 0:
            print(" Time cannot be negative.")
        else:
            break
    except ValueError:
        print(" Invalid number.")
