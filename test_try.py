try:
    age = int(input("How old are you? "))
    print(age + 1)
except ValueError:
    print("Please type your age as a whole number.")

