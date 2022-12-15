"""Play a game of hangman. The computer will randomly pick a word from a list."""
import random
from random_words import words


def valid_word(x_word):
    """Select valid word without dashes or spaces to use for hangman."""
    word = ' '
    while '-' in word or ' ' in word:  # If dash or space is in word, select another word
        word = random.choice(x_word)
    return word.upper()


def hang_state(strike):
    """Return a hangman drawing based off current strikes."""
    hangman_drawn = ['''
       +---+
           |
           |
           |
          ===''', '''
       +---+
       O   |
           |
           |
          ===''', '''
       +---+
       O   |
       |   |
           |
          ===''', '''
       +---+
       O   |
      /|   |
           |
          ===''', '''
       +---+
       O   |
      /|\\  |
           |
          ===''', '''
       +---+
       O   |
      /|\\  |
      /    |
          ===''', '''
       +---+
       O   |
      /|\\  |
      / \\  |
          ===''']
    return hangman_drawn[strike]


def hangman():
    """The actual hangman game."""
    word = valid_word(words)  # Calls on previous valid_word function with 'words' input
    word_letters = set(word)  # Create set of letters of word
    alphabet = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z".split()
    used_letters = set()  # Used letters the user has guessed
    strike = 0

    while len(word_letters) > 0:
        strikes = hang_state(strike)
        print('Strikes: ' + str(strike) + strikes)

        # End program if strikes reaches 6
        if strike == 6:
            print(f'Sorry, you\'re dead. The word was {word}')
            exit()

        # Show letters used separated by spaces
        print('Letters used: ', ' '.join(used_letters))

        # Current word (ie W - R D)
        word_guess = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_guess))

        user_letter = input('Guess a letter: ').upper()
        if user_letter not in alphabet:
            print('Invalid character. Try again.')
        elif user_letter in used_letters:
            print('Letter has already been used. Try again.')
        elif user_letter not in used_letters:
            used_letters.add(user_letter)  # Add to used letters
            if user_letter in word_letters:
                word_letters.remove(user_letter)  # Remove guessed letter from word letter set
            else:
                strike += 1

        print('')
    return word


play = hangman()

print(f'You\'ve correctly guessed the word {play}. You win!')
