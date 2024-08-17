import random as r

word_list = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon", "mango", "nectarine", "orange", "papaya", "quince", "raspberry", "strawberry", "tangerine", "ugli", "vanilla", "watermelon", "xigua", "yellowfruit", "zucchini", "apricot", "blackberry", "coconut", "dragonfruit", "eggplant", "feijoa", "guava", "huckleberry", "imbe", "jackfruit", "kumquat", "lime", "mulberry", "nutmeg", "olive",  "pineapple", "quinoa"]

word = r.choice(word_list).lower()
word_length = len(word)

guessed_letters = []
attempts = word_length + 1

print("Welcome to Hangman!!\n")
print(f"You have {attempts} total attempts.")

while True:
    display = ""  # display the current state of the word
    
    # building the display string to show the user the current state of the word
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    
    print(display)  # print the current state of the word
    
    # checking win condition
    if display == word:
        print("Congratulations! You won.")
        break
    
    guess = input("Guess a letter: ").lower()  # taking a guess from the user
    
    # checking if the letter is in the word
    if guess in word:
        # checking if the guessed letter is already guessed previously
        if guess in guessed_letters:
            print(f"You have already guessed: {guess}")
        else:
            print("Correct")
            guessed_letters.append(guess)
    else:
        print("Incorrect")
        attempts -= 1
        print(f"You have {attempts} attempts left.")
        
        # checking lose condition
        if attempts == 0:
            print(f"You lose.\nThe word was {word}.")
            break
