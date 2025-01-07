import random

characters = input("How many characters should your passwords be? ")
passwords = input("How many passwords would you like? ")

i = 0
while i < int(passwords):
    num = random.random()
    x = 10
    x = x ** int(characters)
    num = num * x
    print(int(num))
    i = i + 1