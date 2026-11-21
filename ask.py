name = input("What is your name? ")
print(f"Hello, {name}!")
try:
    age = int(input("How old are you? "))
    print(f"You will be {age + 1} next year.")
except ValueError:
    print("Please type your age as a whole number.")
