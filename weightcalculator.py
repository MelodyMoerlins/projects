choice = input("Caculate FROM Kilograms or Pounds?").upper()

if choice == "KILOGRAMS":
    numb = input("weight in KG?")
    pound = int(numb) / .45
    pound = int(pound)
    print(f"{numb} LBS is {pound} KG")
elif choice == "POUNDS":
    numb = input("weight in pounds?")
    kg = int(numb) * .45
    kg = int(kg)
    print(f"{numb} LBS is {kg} KG")
else:
    print("Please choose either Kilograms or Pounds.")