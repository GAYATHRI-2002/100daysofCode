import random

word_list = ["playground","Waterfall","money"]
word = random.choice(word_list)
print(word)

guess_letter = input("Guess a letter : ").lower()
print(guess_letter)

for i in word:
    if i == guess_letter:
        print("Right")
    else:
        print("Wrong")