import random

friends = ["Meera","Arun","Ram","Veena","Krishna","Dev"]

#option 1
print(random.choice(friends))

#option 2
random_index = random.randint(0,5)
print(friends[random_index])