#random word
import random

words = ["chicken", "football", "hockey", "freddy", "michael"]

print("HELLLOOOO ARE YOU GETTING THIS")

def get_secret_word():
    return random.choice(words)

print("Sam was here")


#prompts the letter from user
def read_letter_from_user():
    input("Select a Letter")
    letter = input('Please enter a letter: ')
    # add validation what if they didn't enter a letter?
    # What if they just pressed enter before typing a letter?
    # What if they typed out more than a letter?
    # What if they entered a number?
    return letter

#make a function for the guessess and do something else


# Display progress by revealing correctly guessed letters 
# and displaying underscores for letters not guess yet
# e.g. secret_word is "horse" and gussed_letters includes ("h", "r", "i", "o")
#      h_r__
# will also display letters guessed so far


def display_progress(secret_word, guesses):

def hangman_board
 ['''
    +---+
    |   |
        |
        |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
        |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
    |   |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
    /|   |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
    /|\  |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
    /|\  |
    /    |
        |
    =========''', '''
    +---+
    |   |
    O   |
    /|\  |
    / \  |
        |
    =========''']
print(hangman_board)


  
def main():
    print(get_secret_word())
    
main() 


