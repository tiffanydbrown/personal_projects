import random

# REPLACE THE WORDS HERE WITH ONES THAT YOU THOUGHT OF (they are probably better)
word_list = ['minecraft', 'roblox', 'ridiculous', 'understanding', 'skibidi']
word = random.choice(word_list)
attempts_remaining = 6
correct_attempts = ['_' for _ in word]
wrong_attempts = []  # Keep track of wrong guesses

def display():
    print("-------------------------------------")
    print("Current word state:")
    print(' '.join(correct_attempts))
    print("Incorrect guesses:")
    print(' '.join(wrong_attempts))
    print("Attempts remaining:",attempts_remaining)

def guess_letter(guess, attempts_remaining):
    if guess in word:
        for i in range(len(word)):
            letter = word[i]
            if letter == guess:
                correct_attempts[i] = guess
    else:
        wrong_attempts.append(guess)
        attempts_remaining -= 1
    return attempts_remaining

while attempts_remaining > 0 and '_' in correct_attempts:
    display()
    guess = input("Please give type a letter: ").lower()
    if guess in wrong_attempts or guess in correct_attempts:
        print("You've already guessed that letter.")
    else:
        attempts_remaining = guess_letter(guess, attempts_remaining)

if '_' not in correct_attempts:
    print("Congratulations! You've guessed the word:", word)
else:
    print("Out of attempts! The word was:", word)