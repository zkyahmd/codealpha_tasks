import random


def get_word():
    with open('words.txt', 'r') as file:
        words = file.read().splitlines()
    return random.choice(words)


def play_game():
    word = get_word()
    attempts = 5
    guessed = set()
    word_list = list(word)
    display = ['_'] * len(word)

    while attempts > 0 and '_' in display:
        print(' '.join(display))
        print(f'Attempts remaining: {attempts}')
        guess = input('Guess a letter: ').lower()

        if len(guess) != 1 or not guess.isalpha():
            print('Invalid input. Please guess a letter.')
            continue

        if guess in guessed:
            print('You have already guessed that letter.')
            continue

        guessed.add(guess)

        if guess in word_list:
            for i, letter in enumerate(word_list):
                if letter == guess:
                    display[i] = guess
        else:
            attempts -= 1

    if '_' in display:
        print(f'\nSorry, you ran out of attempts. The word was {word}.')
    else:
        print(f'\nCongratulations! You guessed the word: {word}')


if __name__ == '__main__':
    play_game()
