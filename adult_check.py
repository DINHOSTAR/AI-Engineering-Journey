try:
    age = int(input("How old are you? "))
    if age >= 18:
        print("You are an adult.")
    else:
        print("You are a minor.")
except ValueError:
    print("Please type only a whole number.")