import sys

try:
    paper_file = open('paper.txt', encoding='utf-8')
    rock_file = open('rock.txt', encoding='utf-8')
    scissors_file = open('scissors.txt', encoding='utf-8')
    paper = paper_file.read()
    rock = rock_file.read()
    scissors = scissors_file.read()
    paper_file.close()
    rock_file.close()
    scissors_file.close()

except (FileNotFoundError, IOError):
    print('Error! Couldn\'t load\\read files with ASCII images!')
    sys.exit()

print(rock)
print(paper)
print(scissors)

menu = True

def menu():
    print()
    print('{:*^16}'.format('/MENU/'))
    print("*              *")
    print("* 1. Paper     *")
    print("* 2. Rock      *")
    print("* 3. Scissors  *")
    print("* 4. Exit game *")
    print('{:*^16}'.format(''))
    print()

def clear():
    print('\n'*500)

    
menu()

while menu:
    choice = input("Enter your choice: ")
    if choice == '1':
        print(paper)
    elif choice == '2':
        print("Rock")
    elif choice == '3':
        print("Scissors")
    elif choice == '4':
        menu = False
        print("Quitting game...Bye!")
        clear()
    else:
        menu()
        print("Please select an item from the menu.")

