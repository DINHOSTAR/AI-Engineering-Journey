try:
    age = int(input("what is your age? "))
    if age >= 18:
        print("you are an adult.")
    elif age >= 13:
        print("you are a teenager.")
    else:
        print("you are a child.")
except ValueError:
    print("Please type your age as a whole number.")