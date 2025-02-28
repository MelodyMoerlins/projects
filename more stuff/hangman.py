import random

words = ["submarine", "spider", "electricity", "hardware", "traffic", "minecraft", "superman", "christmas", "warning", "photograph"]
num = random.random()
num1 = int(num * 10)
word = words[num1]
guess = ""
guesscount = 0
totalguesscount = 0
letters = len(word)

print(f"Your word is {letters} letters long")

while guess != word:
    guess = input("Guess a letter or final guess: ")
    totalguesscount +=1
    if len(guess) > 1:
        print("Final Guess")
        if guess == word:
            print("YOU WIN!" + "You made " + str(totalguesscount) + " gueses.")
            break
        else:
            print("YOU LOSE!" + " You made " + str(totalguesscount) + " guesses.")  
            print(" _____")
            print("|     |")
            print("|    (x)")
            print("|    /|\\")
            print("|    / \\")
            print("|")
            print("|__")
            print("")
            break
        
    if guess not in word:
        guesscount += 1 
        
    if len(guess) < 2:
        if guess in word:
            letterplace = word.index(guess)+1
            print("Letter place is " + str(letterplace))
    
    if guesscount == 1:
        print("WRONG! Guess again.")
        print("")
        print(" _____")
        print("|     |")
        print("|    ( )")
        print("|")
        print("|")
        print("|")
        print("|__")
    elif guesscount == 2:
        print("WRONG! Guess again.")
        print("")
        print(" _____")
        print("|     |")
        print("|    ( )")
        print("|     |")
        print("|")
        print("|")
        print("|__")
    elif guesscount == 3:
        print("WRONG! Guess again.")
        print("")
        print(" _____")
        print("|     |")
        print("|    ( )")
        print("|     |")
        print("|    /")
        print("|")
        print("|__")
    
    elif guesscount == 4:
        print("WRONG! Guess again.")
        print("")
        print(" _____")
        print("|     |")
        print("|    ( )")
        print("|     |")
        print("|    / \\")
        print("|")
        print("|__")
    
    elif guesscount == 5:
        print("WRONG! Guess again.")
        print("")
        print(" _____")
        print("|     |")
        print("|    ( )")
        print("|    /|")
        print("|    / \\")
        print("|")
        print("|__")
    
    elif guesscount == 6:
        print(" _____")
        print("|     |")
        print("|    (x)")
        print("|    /|\\")
        print("|    / \\")
        print("|")
        print("|__")
        print("")
        print("OUT OF GUESSES! YOU LOSE!" + " You made " + str(totalguesscount) + " guesses")
        break