fname = input("Enter your first name:")
lname = input("Enter your last name:")
num = input("Enter your Phone Number:")

f = open("csvfile.csv", "a")
f.write("\n" + fname + ", " + lname + ", " + str(num))
f.close()

f = open("csvfile.csv", "r")
print(f.read())
with open("csvfile.csv", 'r') as file:
    data = " ".join(line.rstrip() for line in file) + "\n"
jsonconv = input("Convert to JSON file?").upper()

if jsonconv == "YES":
    print("Converting to JSON...")
    try:
        j = open("csvfile.json", "w")
        j.write(data)
        j.close()
        print("Your file was converted successfully.")
    except:
        print("We hit an error! Conversion Failed.")
f.close()