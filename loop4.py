import random
secret = random.randint(1, 20)
guesses = 0
while True:
    guess = int(input("Guess a number "))
    guesses += 1

    if guess > secret:
        print("High")
    elif guess < secret:
        print("Low")
    else: 
        print("YOU GOT IT")
        break
print("Total Guess attempt:", guesses)