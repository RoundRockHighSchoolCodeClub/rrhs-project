# rrhs-project
import random 

print("Welcome to Hangman!")
print("Good luck :)")
cont = 'yes'
while cont == 'yes':
    wordBank = ["innocent", "whimsical", "execution", "death", "spelling", "potato", "ditch", "crack", "rhythm", "phone", "rebel", "pot", "blood", "ankle", "baguette", "four", "avocado", "flex", "refrigerator", "arrow", "banana", "aluminum"]
    goalWord = random.choice(wordBank)
    strikes = 6
    blanks = ""
    for i in goalWord:
        blanks += "_"
    while strikes > 0:
        for char in blanks:
            print(char, end = " ")
        print()
        guess = input("Letter: ")
        index = 0
        listBlanks = list(blanks)
        change = 0
        if guess in goalWord:
            if guess in blanks:
                print("you already guessed that, idiot. tsk tsk tsk")
            for char in goalWord:
                if char == guess:
                    listBlanks[index] = guess
                index = index + 1
            blanks = "".join(listBlanks)
            if blanks == goalWord:
                for char in blanks:
                    print(char, end = " ")
                print("")
                print("congrats, this stickman has been spared!")
                strikes = 0
            if guess == goalWord:
                print("correct!")
                break
        else: 
            print("no <3")
            strikes -= 1
            print(str(strikes) + " strikes left until this innocent stickman's death.")
            if strikes == 0:
                print("you lose :(")
                print(goalWord + " was the correct word.")
    print("")
    cont = input("would you like to play again? ")  
print("goodbye.")
