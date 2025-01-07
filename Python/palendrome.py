
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for num in numbers:
    i = 9 - num
    while i > 0:
        print(" ", end="")
        i -= 1 
    num = int(num)
    number = num
    print(num, end="")
    
    while int(num) > 1:
        num = num-1
        print(num, end="")
    
        
    while num < number:
        num += 1
        print(num, end="")
        
    print("")