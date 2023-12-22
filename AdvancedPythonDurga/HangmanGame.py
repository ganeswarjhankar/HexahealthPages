import random
import ImagesHangGame

work_list = ["apple", "beautiful", "potato"]
lives = 6
chosen_word = random.choice(work_list)
print(chosen_word)
display_empty = []
for i in chosen_word:
    display_empty.append('_')

print(display_empty)
game_over = False
while not game_over:
    guessed_letter = input("guess a Letter").lower()  # r
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guessed_letter:
            display_empty[position] = guessed_letter

    print(display_empty)
    if guessed_letter not in chosen_word:
        lives = lives - 1

        print("the remaining lives are", lives)
        #if lives == 1:
        #    print("last chance ", )
        #    continue

        if lives == 0:
            game_over = True
            print("You lose")

    if '_' not in display_empty:
        game_over = True
        print("You win")

    print(generators.stages[lives])






