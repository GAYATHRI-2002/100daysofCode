import random
import hangmanwords
import hangmanarts


print(hangmanarts.logo)
word = random.choice(hangmanwords.word_list)
print(word)
placeholder = ""
lives = 6
for i in range(len(word)):
    placeholder += "-"
print(placeholder)

game_over = False
correct_letter = []
while not game_over:
    guess_letter = input("Guess a letter : ").lower()
    # print(guess_letter)
    display = ""
    if guess_letter in correct_letter:
        print(f"You already guessed {guess_letter} letter... ")
    for i in word:
        if i == guess_letter:
            display += i
            correct_letter.append(i)
        elif i in correct_letter:
            display += i
            correct_letter.append(i)
        else:
            display += "_"
    print(display)

    if guess_letter not in word:
        lives -= 1
        print(f"You gussed the letter {guess_letter}, which is not correct and lost a life..... ")
        print(f"Lives remain is {lives}")
        if lives == 0:
            game_over = True
            print("No lives")

    if "_" not in display:
        game_over = True
        print("You win")

    print(hangmanarts.stages[lives])
