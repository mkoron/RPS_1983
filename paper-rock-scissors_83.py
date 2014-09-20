import sys, time, random

#Load the ASCII images

try:
    intro_file = open('intro.txt', encoding='utf-8')
    paper_file = open('paper.txt', encoding='utf-8')
    rock_file = open('rock.txt', encoding='utf-8')
    scissors_file = open('scissors.txt', encoding='utf-8')
    banner_file = open('banner.txt', encoding='utf-8')
    intro = intro_file.read()
    banner = banner_file.read()
    paper = paper_file.read()
    rock = rock_file.read()
    scissors = scissors_file.read()
    intro_file.close()
    banner_file.close()
    paper_file.close()
    rock_file.close()
    scissors_file.close()

except:
    print('Error! Couldn\'t load\\read files with ASCII images!')
    print('You must download all the "txt" files and place them in the same folder as the "paper-rock-scissors_83.py" file.')
    sys.exit()

#Global variables
    
Y_SCORE = 0
C_SCORE = 0
MENU = True
CHOICES = {1:rock, 2:paper, 3:scissors}
WINNER = {0:"It's a tie!", 1: "You win!", 2:"You lose!"}

#Functions

def splash_screen():
    """
    Prints the splash_screen of the game.
    """
    clear()
    print("Best viewed in full-screen")
    print("loading", end="")
    for item in "...":
        print(item, end="") 
        time.sleep(1)
    clear()
    print(intro)
    input("")
    clear()


def gameLogic(y_choice, c_choice):
    """ 
    Receives the user and computer choices and performs a modulo arithmetic (modulo 3)
    to determine the winner or a tie results.
    """
    global Y_SCORE, C_SCORE
    result = (y_choice - c_choice) % 3
    print(WINNER[result])
    if result == 1:
        Y_SCORE += 1
    elif result == 2:
        C_SCORE += 1
    

def computerChoice():
        """
        Returns a random number in range [1-3].
        """ 
        return random.randint(1,3)

def menu():
    """
    Displays the menu of the game.
    """
    print()
    print(banner)
    print('{:*^16}'.format('/MENU/'))
    print("*              *")
    print("* 1. Rock      *")
    print("* 2. Paper     *")
    print("* 3. Scissors  *")
    print("* 4. Rules     *")
    print("* 5. Exit game *")
    print('{:*^16}'.format(''))
    print()

def clear():
    """
    Clears the screen with 500 new lines.
    """
    print('\n'*500)

def animation(key1, key2):
    """
    Performs a simple animation based on the player and computer choices.
    """
    print("\nFight!\n")
    time.sleep(1)
    vs = ("Your choice: " +"\n" + CHOICES[key1] + "\n\n\n" + '{:*^16}'.format('') + "vs." 
         + '{:*^16}'.format('') + "\n\n\n" + "Computer's choice: " + "\n"
         + CHOICES[key2] + "\n\n")

    for item in vs:
        print(item, end="") 

def scoreBanner():
    """
    Displays the current score in the game.
    """
    clear()
    print('{:-^105}'.format(''))
    score = "\n" + " ***Score*** \n\n" + " You:  " + str(Y_SCORE) + "\n Comp: " + str(C_SCORE)
    print(score, end="")

#Start game
         
clear()
splash_screen()
menu()             

#Menu loop

while MENU:
    choice = input("Enter your choice: ")
    if choice == '1' or choice == '2' or choice == '3':
        y_choice = int(choice)
        c_choice = computerChoice()
        animation(y_choice, c_choice)
        gameLogic(y_choice, c_choice)
        time.sleep(2)
        scoreBanner()
        menu()
    elif choice == '4':
        print("Yeah right, you DON'T know the rules of this game...")
    elif choice == '5':
        MENU = False
        print("Quitting game...Bye!")
        time.sleep(1.5)
        clear()
    else:
        menu()
        print("Please select an item from the menu.")


