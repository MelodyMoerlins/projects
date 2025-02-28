action = input("see, add, or use? ").lower()

if action == "see":
    f = open("inventory.csv")
    print(f.read())
    f.close()
elif action == "add":
    f = open("inventory.csv", "a")
    i = input("what would you like to add? ").lower()
    i = i + ", \n"
    f.write(i)
    f.close()
elif action == "use":
    i = open("inventory.csv", "r")
    data = i.readlines()
    f = open("inventory.csv", "w")
    u = input("what would you like to use? ").lower()
    u = u + ", \n"
    for line in data:
        if line.strip("/n") != u:
            f.write(line)
    i.close
    f.close
