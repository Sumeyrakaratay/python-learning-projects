import random

gameTitle = "Word Hunter"

with open("words.txt", "r", encoding="utf-8") as f:
    words = [w.strip().lower() for w in f.readlines() if len(w.strip()) == 5]

if not words:
    print("No 5-letter words found in words.txt.")
    exit()


secretWord = random.choice(words).lower()

#Game Variables
attempts = 5
wrongLetters = []       # Letters not in the word
misplacedLetters = []   # Letters in the word but in wrong position

print(f"🎮 Welcome to {gameTitle}!")
print("You have 5 attempts to guess the 5-letter word.\n")

#Game Loop
for attempt in range(1, attempts + 1):
    suffix = "th"
    if attempt == 1: suffix = "st"
    elif attempt == 2: suffix = "nd"
    elif attempt == 3: suffix = "rd"
    guess = input(f"{attempt}{suffix} guess (5 letters): ").lower()

    #Invalid input check
    if len(guess) != 5:
        print("Please enter a 5-letter word!\n")
        continue

    #Analyze guess
    display = ""
    for i in range(5):
        if guess[i] == secretWord[i]:
            display += guess[i]  # Correct letter, correct position
        elif guess[i] in secretWord:
            display += "_"       # Correct letter, wrong position
            if guess[i] not in misplacedLetters:
                misplacedLetters.append(guess[i])
        else:
            display += "_"       # Incorrect letter
            if guess[i] not in wrongLetters:
                wrongLetters.append(guess[i])

    
    print("Result:", display)
    print("Misplaced letters:", misplacedLetters)
    print("Wrong letters:", wrongLetters, "\n")


    if guess == secretWord:
        print(f"🎉 Congratulations! You guessed the word: {secretWord}")
        break
else:
    print(f"😢 You've used all attempts. The correct word was: {secretWord}")
