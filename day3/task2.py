print("Welcome to Python Pizza Deliveries")
size = input("What size pizza do you want? S M or L: ")
bill = 0
if size == "S":
    bill = bill + 15
elif size == "M":
    bill = bill + 20
elif size == "L":
    bill = bill + 25

pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
if size == "S" and pepperoni == "Y":
    bill = bill + 2
elif size == "M" or size == "L" and  pepperoni == "Y":
    bill = bill + 3

extra_cheese = input("Do you want extra cheese? Y or N: ")
if extra_cheese == "Y":
    bill = bill + 3
    print(f"Your final bill is {bill}")
elif extra_cheese == "N":
    print(f"your final bill is {bill}")



