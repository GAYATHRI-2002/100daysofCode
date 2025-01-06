#picking a random word and guess it

word_list = ["apple","energy","elephant","waterfall"]
guess = input("Enter a letter: ").lower()
for i in word_list:
    if guess == i:
        print(f"The word {guess} is in the list")
        break
else:
    print("No")