import random
import string

words = ["cupboard", "pillow", "coffee", "maker", "bed", "spoon", "blanket",
         "knife", "stove", "sink", "washing", "machine", "pot", "dish", "fridge",
         "sofa", "stool", "cup", "fork", "glass", "computer", "notebook", "desk",
         "pencil", "bookcase", "book", "chair", "backpack", "paper", "glue",
         "door", "ruler", "clock", "whiteboard", "window", "bicycle", "banknote",
         "wallet", "blouse", "bag", "shirt", "helmet", "toothbrush", "key", "table",
         "coin", "trousers", "pants", "sweater", "shoe"]

word = random.choice(words)
wordletter = set(word)  # Store the letters of the word in a set
lives = 8

print("Welcome to hangman")
print("Try to guess the word, all a things")


alphabet = set(string.ascii_lowercase)
used_letter = set()


# Create a list to store the revealed characters (initially all underscores)
revealed_chars = ['_' if letter.isalpha() else letter for letter in word]

while lives > 0 and '_' in revealed_chars:
    print(" ".join(revealed_chars))
    print("Lives:", lives)
    guess = input("Make a guess: ").lower()
    
    if guess in alphabet - used_letter:
        used_letter.add(guess)
        if guess in wordletter:
            for i, letter in enumerate(word):
                if letter == guess:
                    revealed_chars[i] = guess
        else:
            lives -= 1
            print(guess, "is not present in the word")

    elif guess in used_letter:
        print("You have already guessed this letter.")
    else:
        print("Invalid input.")

if "_" not in revealed_chars:
    print("You win! The word is:", word)
else:
    print("You lose! The word was", word)