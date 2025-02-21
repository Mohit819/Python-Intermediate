import random as r
lives = 7
words = ['pizza', 'fairy', 'teeth', 'shirt', 'table', 'plane']
secret_word = r.choice(words)
clue = list("?????")
heart_symbol = u'\u2764'
guessed_word_correctly = False
def update_clue(guessed_letter,secret_word,clue):
    index = 0
    while index < len(secret_word):
        if guessed_letter == secret_word[index]:
            clue[index] = guessed_letter
        index += 1
while lives > 0:
    print(clue)
    print("Lives left:"+ heart_symbol * lives)
    guess = input("Guess a letter or the whole word:")

    if guess == secret_word:
        guessed_word_correctly = True
        break
    
    if guess in secret_word:
        update_clue(guess, secret_word, clue)
    else:
        print("Incorrect. You lose a life")
        lives -= 1
if guessed_word_correctly == True:
    print("You Won! You're Sigma! The secret word was "+secret_word)
else:
    print("You Lost! You're Skibidi! The secret word was "+secret_word)