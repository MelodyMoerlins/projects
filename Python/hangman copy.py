import random

words = ["submarine", "spider", "electricity", "hardware", "traffic", "minecraft", "superman", "christmas", "warning", "photograph"]
word = words[int(random.random()*10)]
guess = ""
totalguesscount = 0
letters = len(word)
u = ""

for letters in word:
    u+="_"
print(u)

#plays if you run out of moves or fail to guess the word
def youlose():
    print(" _____")
    print("|     |")
    print("|    (x)")
    print("|    /|\\")
    print("|    / \\")
    print("|")
    print("|__")
    print("")
    print("YOU LOSE! Your word was \"" + word +"\"")

while guess != word:
    guess = input("Guess a letter or final guess: ")
    if len(guess) > 1:
        print("Final Guess")
        if guess == word:
            print("YOU WIN!" + "You made " + str(totalguesscount+letters) + " guesses.")
            break
        else:
            youlose()
            break
        
    if guess not in word:
        #adds to guesscount
        totalguesscount += 1
        if totalguesscount <6:
            print("WRONG! Guess again.")
            print(u)
            print("")
            print(" _____")
            print("|     |")
            print("|    ( )")
        
    if len(guess) < 2:
        if guess in word:
            letterplace = word.index(guess)
            u = u[:letterplace] + guess + u[letterplace+1:]
            print(u)

    #displays the hangman visually in the console
    if totalguesscount == 1:
        print("|")
        print("|")
        print("|")
        print("|__")
    elif totalguesscount == 2:
        print("|     |")
        print("|")
        print("|")
        print("|__")
    elif totalguesscount == 3:
        print("|     |")
        print("|    /")
        print("|")
        print("|__")
    
    elif totalguesscount == 4:
        print("|     |")
        print("|    / \\")
        print("|")
        print("|__")
    
    elif totalguesscount == 5:
        print("|    /|")
        print("|    / \\")
        print("|")
        print("|__")
    
    elif totalguesscount == 6:
        youlose()
        break
