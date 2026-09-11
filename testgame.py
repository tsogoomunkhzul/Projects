from random import randint
 
target = randint(1, 20)
guesses = 0
 
while True:
    raw = input("Guess a number from 1 to 20: ").strip()
 
    if not raw.isdigit() or not 1 <= int(raw) <= 20:
        print("Enter a whole number from 1 to 20.")
        continue
 
    guess = int(raw)
    guesses += 1
 
    if guess < target:
        print("Too low.")
    elif guess > target:
        print("Too high.")
    else:
        word = "guess" if guesses == 1 else "guesses"
        print(f"You got it in {guesses} {word}.")
        break