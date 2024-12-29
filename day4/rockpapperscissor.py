from random import choice

computer_choice = ["rock","paper","scissors"]
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
print("################################################################################################################")
print("Welcome to the rock paper scissor game.Enter your signal \nfor rock enter R,for paper enter P,for scissors enter S")
print("Computer will generate its own random choice")
print("################################################################################")
print("The rules are\nRock wins against scissors.\nScissors win against paper.\nPaper wins against rock.")
print()


signal = input("enter your choice: ").upper()
if signal == "R":
    print(f"your choice is rock {rock}")
elif signal == "P":
    print(f"your choice is paper {paper}")
elif signal == "S":
    print(f"your choice is scissors {scissors}")

random_choice = choice(computer_choice)
# print(random_choice)
if random_choice == "rock":
    print(f"Computer choice is rock {rock}")
    if signal == "R":
        print("DRAW")
    elif signal == "P":
        print("You won")
    elif signal == "S":
        print("computer won")

elif random_choice == "paper":
    print(f"Computer choice is paper {paper}")
    if signal == "R":
        print("Computer won")
    elif signal == "P":
        print("DRAW")
    elif signal == "S":
        print("you won")

else:
    print(f"Computer choice is scissors {scissors}")
    if signal == "R" and random_choice == "scissors":
        print("You won")
    elif signal == "P" and random_choice == "scissors":
        print("computer won")
    elif signal == "S" and random_choice == "scissors":
        print("DRAW")