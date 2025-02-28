import random

characters = input("How many characters should your passwords be? ")
passwords = input("How many passwords would you like? ")
digits = ["1","2","3","4","5","6","7","8","9","0","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","!","@","#","&","*","$","%"]
numberof = int(characters)
i = 0
s = ""
while i < int(passwords):
    numberof = int(characters)
    while numberof > 0:
        num = random.choice(digits)
        s = s + num
        numberof = numberof - 1
    i = i+1
    print(s)
    s = ""