import random
import sys

def guess_sort(guessed):
    """Function to add guesses to the list and then sort the list"""
    guesses.append(guessed)
    guesses.sort()
    return None

def pick_word(file_name):
    """Opens the file and reads the word list for a word to be picked"""
    word_list = []
    with open(file_name, "r") as hgm:
        for line in hgm:
            line = line.split()
            word_list.append(str.strip(line[0])) #takes the words and puts it in a list
    return word_list[random.randint(0, len(lines))] #picks a random word from the list

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
    return None

def print_display(visual, limbs_lost, list_of_guesses):
    """prints out the information for the player"""
    print("\n" + " ".join(visual))
    print("lives remaining:", limbs_lost)
    print("you have guessed", ", ".join(list_of_guesses))
    return None

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
lines = []
guesses = []
found = []
lives = 7

#Starts game
print("H A N G M A N")
word = pick_word("Hgm.txt")
print("the word has", len(word), "letters.")
picture = ["_"] * len(word)
print(" ".join(picture)) #makes the "picture" for the user to see

#Game loop
while lives > 0:
    if picture.count("_") == 0:  #checks if there are any empty spaces left
        print()
        print("congratulations! you won!")
        sys.exit()
    else:
        #Inputs a new guess
        guess = input("what is your guess?\n")[0]
        if guess == "":
            print("Don't just hit enter, guess something!")
            continue
        x = 0
        index = []
        # finds all occurrences of the guessed letter in the word
        while word.find(guess, x) != -1:
            x = word.find(guess,x) + 1
            if x > 0:
                index.append(x - 1)
        #Removes a life if the guess isn't in the word, otherwise adds it to the list of found words
        if guesses.count(guess):
            print("you already guessed this letter!")
        #failsafes if the player doesn't type a letter
        elif letters.count(guess) == 0:
            print("type a letter ya goof")
        elif not len(index): #if the word wasn't found
            lives -= 1
            guess_sort(guess)
            print("you guessed incorrectly.")
        #adds the items to the word
        else:
            guess_sort(guess)
            for item in index:
                found.append(item)
                picture[item] = guess

        #Prints the display
        print_display(picture, lives, guesses)

        #draws out the hangman
        draw_hangman(lives)

print("you lose, better luck next time.")
print("the word was",word)
