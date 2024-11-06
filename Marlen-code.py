# Do not delete this line!
from wordle_helpers import select_random_word, print_color


WORD_LIST = [
    "HEART",
    "DOORS",
    "REACH",
    "BEACH",
    "FETCH",
]





# Do not change this function name!
def main():
    wordle = select_random_word()

    # Your code here.
    player_turn = 0
    while player_turn< 6:

        user_guess = input("Enter a guess: ")
        user_guess_length = len(user_guess)

    #user guess length is 5 letter long
        while user_guess_length != 5:
            print("Word is invalid!")
            user_guess = input("selct a new word: ")
            user_guess_length = len(user_guess)

        user_guessL = user_guess.lower()
        wordle_low = wordle.lower()
    #
        guess_list = list(user_guessL)

        wordle_list = list(wordle_low)
        #print(wordle_list)
        #print(guess_list)

    #how to compare each letter in the list to the string
    #it
        for compare_word in range(5):
            if wordle_list[compare_word]== guess_list[compare_word]:
                print_color(guess_list[compare_word], "GREEN")
            elif guess_list[compare_word] in wordle_list:
                print_color(guess_list[compare_word], "YELLOW")
            else:
                print_color(guess_list[compare_word], "BLACK")
        print()
# after that look to use print color function^^

        player_turn += 1

        #win condition
        if guess_list == wordle_list:
            print("you got it!")
            break
        elif player_turn == 6:
            print("sorry the word was: " + wordle_low)




    #if input == select_random_word():
        #print("print_color("a", "green")")

    
#for attempt in range(1, 7):
    # print_color will print a single character in the specified color


    # print_color("a", "GREEN")


# Comment this out when submitting for tests!

#main()

