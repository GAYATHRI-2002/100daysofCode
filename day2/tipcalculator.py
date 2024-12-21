print("Welcome to tip calculator!")
bill = float(input("What was the total bill? Rs"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
tippercent = tip / 100
people = int(input("How many people to split the bill? "))
total_tip_amount = bill * tippercent
result = total_tip_amount + bill
bill_per_person = result / people
print(f"Each person should pay {round(bill_per_person,2)}")



