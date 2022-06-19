from random import randint, randrange

entrances_left = 3
descriptions_left = 3

def task_description():
    print("\n\t***WELCOME TO THE ESCAPE ROOM!***")
    print("____________________________________________________")
    print("|                   |              |               |")
    print("|                   |              |               |")
    print("|        \U0001F40D         |      \U0001F977       |      \U0001F42F       |")
    print("|                   |              |               |")
    print("|______________   __|______   _____|_   ___________|")
    print("|                                               \U0001F613 |")
    print("|         |_______   ____________   __________   __|")
    print("|         |               |                |       |")
    print("          |               |                |       |")
    print("   \U0001F3C3     |      \U0001F9DB       |      \U0001F9DF        |  \U0001F479   |")
    print("|         |               |                |       |")
    print("|_________|_______________|________________|_______|")

    print("\n\n\tOne dark rainy night your car broke down in the middle of an unfamiliar road. \
There was nothing you could do, no one you could call. \
Suddenly, the weather became impossibly cold and you had to leave the car and find a shelter to stay warm. \
There was a big house a kilometer away. You ran to that house without thinking. \
Once you entered the house, you realized you had made a mistake: someone started laughing loudly \
and fearsomely and the door shut behind your back. \
Then you heard the rules echoing throughout the house: \
there is only one room out of seven from which you can escape. \
You have 3 tries to choose the room that you think will set you free \
and you can get descriptions about 3 rooms. \
If you pick the wrong room 3 times in a row, you will die from the danger lurking there.")

    print("\nThere is a map of your 'prison': ")
    print("____________________________________________________")
    print("|                   |              |               |")
    print("|                   |              |               |")
    print("|         5         |      6       |       7       |")
    print("|                   |              |               |")
    print("|______________   __|______   _____|_   ___________|")
    print("|                                          YOU ARE |")
    print("|         |_______   ____________   _________HERE__|")
    print("|    4    |               |                |       |")
    print("|         |               |                |       |")
    print("|         |       3       |       2        |   1   |")
    print("|         |               |                |       |")
    print("|_________|_______________|________________|_______|")

    print("\n*Your task is to leave the house alive*")


def get_users_choice():
    while True:
        try:
            users_choice = int(input("\nEnter your choice: "))
            if users_choice >= 1 and users_choice <=3:
                return users_choice
            else:
                print("There was no such choice. Try again:") 
        except ValueError:
            print("There was no such choice. Try again:")


if __name__ == "__main__":

    task_description()

    should_continue = True
    while should_continue:
        escape_room = randint(1, 7)
        print(f"*Escape room is: {escape_room}*")

        while True:
            print("__________________________________________________________________________________")
            print("\nChoose one of the options below:")
            print("1 - enter to a specific room")
            print("2 - get a description of a specific room")
            print("3 - check how many tries to enter the room and to get descriptions you have left")
            
            choice = get_users_choice()
            if choice == 1:
                if entrances_left == 3 or entrances_left == 2:
                    chosen_room = int(input("Which room from 1st to 7th do you want to enter? "))
                    if chosen_room < 1 and chosen_room > 7: 
                        print("There is no such room. Check your input and try again: ")
                    elif chosen_room != escape_room:
                        print("\n*You chose the wrong room but you were quick enough to leave before you got into the danger lurking behind those doors*")
                    elif chosen_room == escape_room:
                        print("\n***You have escaped the house! RUN AND NEVER COME BACK***")
                        should_continue = False
                        break
                    

                    entrances_left = entrances_left - 1
                    
                elif entrances_left == 1:
                    print("*If you choose wrong room, you die*")
                    chosen_room = int(input("Which room from 1st to 7th do you want to enter? "))
                    if chosen_room != escape_room and chosen_room >= 1 and chosen_room <= 7:
                        print("\n***GAME OVER! You chose the wrong room and died***")
                    elif chosen_room == escape_room:
                        print("\n***You have escaped the house! RUN AND NEVER COME BACK***")
                    else:
                        print("\nThere is no such room. Check your input and try again:")
                        continue

                    should_continue = False
                    break

            elif choice == 2:
                
                if descriptions_left == 2 or descriptions_left ==3:
                    chosen_room_for_description = int(input("About which room from 1st to 7th do you want to get a description? "))
                    if chosen_room_for_description == escape_room:
                        print("\nNo one saw a man returning from this room.")
                    elif chosen_room_for_description != escape_room:
                        print ("\nThis room will not take you anywhere else but to death.")
                    else:
                        print("\nThere is no such room. Check your input and try again:")
                        chosen_room_for_description = int(input("About which room from 1st to 7th do you want to get a description? "))

                    descriptions_left = descriptions_left - 1

                elif descriptions_left == 1:
                    print("*This is your last description about a room*")
                    chosen_room_for_description = int(input("About which room from 1st to 7th do you want to get a description? "))
                    if chosen_room_for_description == escape_room:
                        print("\nNo one saw a man returning from this room.")
                    elif chosen_room_for_description != escape_room:
                        print ("\nThis room will not take you anywhere else but to death.")
                    else:
                        print("\nThere is no such room. Check your input and try again:")
                        chosen_room_for_description = int(input("About which room from 1st to 7th do you want to get a description? "))
                    descriptions_left = descriptions_left - 1

                elif descriptions_left == 0:
                    print("\n*You have used all 3 descriptions*")
                
            elif choice == 3:
                print(f"Entrances left: {entrances_left}")
                print(f"Descriptions left: {descriptions_left}")

            else:
                print("There was no such choice, check your input and try again:")
                choice = input("\nEnter your choice: ")
                print(choice)
        