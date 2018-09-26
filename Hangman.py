import random
import sys
alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
lines = []
guesses = []
found = []
space = "_"
s = " "
comma = ", "
lives = 7
in_file = open("Hgm.txt", "rt")
with open("Hgm.txt", "rt"):   #opens and reads the word list
    for line in in_file:
        line = line.split()
        lines.append(str.strip(line[0])) #takes the words and puts it in a list
word = lines[random.randint(0, 1525)] #picks a random word from the list
print("H A N G M A N")
print("the word has", len(word), "letters.")
picture = [space] * len(word) #makes the "picture" for the user to see
print(s.join(picture))
while lives > 0:
    if picture.count(space) == 0:  #checks if there are any empty spaces left
        print("congratulations! you have won!")
        print("   ----      ----  ")
        print("  (  * )     (  * )")
        print("                   ")
        print("          ^        ")
        print("      \_______/    ")
        sys.exit()
    else:
        guess = input("what is your guess?\n")
        guess = guess[:1]
        fin = word.find(guess)
        fins = word.find(guess,fin + 1)
        fint = word.find(guess,fins + 1)
        if guesses.count(guess) > 0:
            print("you already guessed this letter!")
        elif alpha.count(guess) == 0:
            print("type a letter ya goof")
        elif fin < 0:
            lives -= 1
            guesses.append(guess)
            guesses.sort()
            print("you guessed incorrectly.")
        elif fin >= 0 and fins < 0:
            guesses.append(guess)
            guesses.sort()
            found.append(fin)
            picture[fin] = guess
        elif fin >= 0 and fins >= 0 and fint < 0:
            guesses.append(guess)
            guesses.sort()
            found.append(fin)
            found.append(fins)
            picture[fin] = guess
            picture[fins] = guess
        else:
            guesses.append(guess)
            guesses.sort()
            found.append(fin)
            found.append(fins)
            found.append(fint)
            picture[fin] = guess
            picture[fins] = guess
            picture[fint] = guess
        print()
        print(s.join(picture))
        print("lives remaining:", lives)
        print("you have guessed", comma.join(guesses))
        if lives == 6:
            print(" ______    ")
            print("|      |   ")
            print("|  ")
            print("|  ")
            print("|  ")
            print("|  ")
            print("|__________")
        elif lives == 5:
            print(" ______    ")
            print("|      |   ")
            print("|      O")
            print("|    ")
            print("|    ")
            print("|    ")
            print("|__________")
        elif lives == 4:
            print(" ______    ")
            print("|      |   ")
            print("|    __O")
            print("|        ")
            print("|        ")
            print("|   ")
            print("|__________")
        elif lives == 3:
            print(" ______    ")
            print("|      |   ")
            print("|    __O__ ")
            print("|      ")
            print("|      ")
            print("|      ")
            print("|__________")
        elif lives == 2:
            print(" ______    ")
            print("|      |   ")
            print("|    __O__ ")
            print("|      |   ")
            print("|      ^   ")
            print("|   ")
            print("|__________")
        elif lives == 1:
            print(" ______    ")
            print("|      |   ")
            print("|    __O__ ")
            print("|      |   ")
            print("|      ^   ")
            print("|     /  ")
            print("|__________")
        elif lives == 0:
            print(" ______    ")
            print("|      |   ")
            print("|    __O__ ")
            print("|      |   ")
            print("|      ^   ")
            print("|     / \\ ")
            print("|__________")
print("you lose, better luck next time.")
print("the word was",word)



