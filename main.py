import random
import jhn
import saer

version = "____________________________________________________________________________________________________________"

print(jhn.logo)

# To Randomly choose a word from the word_list and assign it to  a variable called chosen_word.

chosen_word = random.choice(saer.word_list)
print(chosen_word)
# print(f"the chosen letter is {chosen_word}")

print(version)
# To Ask the user to guess a letter and assign their answer to a variable called guess  .Make guess lower case.
display = []
for _ in chosen_word:  # we can use "_" this as a stand in variable.
    display.append("_")
print(display)

print(version)
word_length = len(chosen_word)
lives = 6
end_of_game = False

while not end_of_game:

    guess = input(str("Guess a letter:\n").lower())

    # To check if the letter of the user guessed (guess) is one of the letters of the chosen word.

    for position in range(word_length):

        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("End of Game\nYou Lose")

    print(f'{" ".join(display)}')

    if "_" not in display:
        print("You Have win")
        break  # or use end_of_game = True

    print(jhn.stages[lives])
