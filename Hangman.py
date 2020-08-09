from random import randint

LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
           'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def add_guess_and_sort(guessed, guesses):
    """Function to add guesses to the list and then sort the list"""
    guesses.append(guessed)
    guesses.sort()


def pick_word(file_name):
    """Opens the file and reads the word list for a word to be picked"""
    word_list = []
    with open(file_name, "r") as hgm:
        for line in hgm:
            line = line.split()
            # takes the words and puts it in a list
            word_list.append(str.strip(line[0]))
    # picks a random word from the list
    return word_list[randint(0, len(word_list) - 1)]


def find_letters_in_word(index, guess, word):
    """finds all occurrences of the guessed letter in the word"""
    x = word.find(guess, 0)
    while x >= 0:
        index.append(x)
        x += 1
        x = word.find(guess, x)


def draw_hangman(limbs_lost):
    """prints out the visual for the hangman"""
    if limbs_lost < 7:
        print(" ______    ")
        print("|      |   ")
        if limbs_lost == 6:
            print("|          ")
        if limbs_lost == 5:
            print("|      O   ")
        if limbs_lost == 4:
            print("|    __O   ")
        if limbs_lost <= 3:
            print("|    __O__ ")
        if limbs_lost > 2:
            print("|          ")
            print("|          ")
            print("|          ")
        else:
            print("|      |   ")
            print("|      ^   ")
        if limbs_lost == 1:
            print("|     /    ")
        if limbs_lost == 0:
            print("|     / \\ ")
        print("|__________")


def print_display(visual, limbs_lost, list_of_guesses):
    """prints out the information for the player"""
    print("\n" + " ".join(visual))
    print("lives remaining:", limbs_lost)
    print("you have guessed", ", ".join(list_of_guesses))


def hangman_game(word_list):
    """game of hangman! try to guess the word without letting your guy die"""
    guesses = []
    lives = 7

    # Starts game
    print("H A N G M A N")
    word = pick_word(word_list)
    print("the word has", len(word), "letters.")
    picture = ["_"] * len(word)
    print(" ".join(picture))  # makes the "picture" for the user to see

    # Game loop
    while lives > 0 and picture.count("_") != 0:
        # Inputs a new guess
        guess = input("what is your guess?\n")
        if not guess:
            print("Don't just hit enter, guess something!")
            continue
        guess = guess[0].lower()
        if guess not in LETTERS:
            print("type a letter ya goof")
            continue
        elif guess in guesses:
            print("you already guessed this letter!")
            continue

        index = []
        find_letters_in_word(index, guess, word)

        if len(index) == 0:  # if the letter wasn't found in word
            lives -= 1
            print("you guessed incorrectly.")
        else:  # adds the items to the word
            for item in index:
                picture[item] = guess
        add_guess_and_sort(guess, guesses)

        # Prints the display
        print_display(picture, lives, guesses)

        # draws out the hangman
        draw_hangman(lives)

    if not picture.count("_"):
        print()
        print("congratulations! you won!")
    else:
        print("you lose, better luck next time.")
        print("the word was", word)


hangman_game('Hgm.txt')
