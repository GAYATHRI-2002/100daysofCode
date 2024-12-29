import random

# print(random.randint(1,4))
# print(random.random() * 3)

random_head_or_tail = random.randint(0,1)
if random_head_or_tail == 0:
    print("Head")
else:
    print("Tail")