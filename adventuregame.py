print("Welcome to the Adventure Game ")
print("Your goal is to escape the haunted house.")
print("You find yourself in a dark room with two doors.")

# Player's first choice
choice1 = input("Do you want to go through the left door or the right door? (left/right): ").upper()

if choice1 == 'RIGHT':
    print("You enter a room with a old piano.")
    # Player's second choice
    choice2 = input("Do you want to play the piano or exit the room? (play/exit): ").upper()

    if choice2 == 'PLAY':
        print("You play a haunting melody, and a secret passage opens. You escape the house! YOU WIN!")
    elif choice2 == 'EXIT':
        print("You exit the room and fall into a trap door. GAME OVER!")
    else:
        print("Invalid choice. GAME OVER!")

elif choice1 == 'LEFT':
    print("You enter a dimly lit room with a bookshelf.")
    # Player's second choice
    choice2 = input("Do you want to pull a book from the shelf or look under the table? (pull/look): ").upper()

    if choice2 == 'PULL':
        print("You pull a book and the bookshelf rotates, revealing an exit. You escape the house! YOU WIN!")
    elif choice2 == 'LOOK':
        print("You look under the table and a ghost appears! GAME OVER!")
    else:
        print("Invalid choice. GAME OVER!")

else:
    print("Invalid choice. GAME OVER!")
