def get_int(prompt):
    try:
        return int(input(prompt))
    except:
        print("Invalid input. Try again.")
        return None


def english_menu():
    while True:
        print("""
Welcome to the 3310 phone program
1. PhoneBook
2. Messages
3. Chat
4. Call register
5. Tones
6. Settings
7. Call divert
8. Games
9. Calculator
10. Reminders
11. Clock
12. Profiles
13. SIM services
0. Back
""")

        main_option = get_int("Enter your choice: ")
        if main_option is None:
            continue
        if main_option == 0:
            return

        match main_option:
            case 1:
                phonebook_menu()
            case 2:
                messages_menu()
            case 3:
                print("You selected Chat")
            case 4:
                call_register_menu()
            case 5:
                print("You selected Tones")
            case 6:
                settings_menu()
            case 7:
                print("You selected Call divert")
            case 8:
                print("You selected Games")
            case 9:
                print("You selected Calculator")
            case 10:
                print("You selected Reminders")
            case 11:
                print("Clock menu")
            case 12:
                print("Profiles")
            case 13:
                print("SIM services")
            case _:
                print("Invalid option")


def phonebook_menu():
    while True:
        print(""" 
PHONEBOOK
1. Search
2. Service Nos.
3. Add name
4. Erase
5. Edit
6. Assign tone
7. Send b'card
8. Options
9. Speed dials
10. Voice tags
0. Back
""")

        c = get_int("Enter your choice: ")
        if c is None:
            continue
        if c == 0:
            return

        match c:
            case 8:
                print("Options\n1. Type of view\n2. Memory status")
            case _:
                print("Invalid option")


def messages_menu():
    while True:
        print("""
MESSAGES
1. Write messages
2. Inbox
3. Outbox
4. Picture messages
5. Templates
6. Smileys
7. Message settings
8. Info service
9. Voice mailbox
10. Service command editor
0. Back
""")

        c = get_int("Enter your choice: ")
        if c is None:
            continue
        if c == 0:
            return

        match c:
            case 7:
                print("Message settings\n1. Set 1\n2. Common")
            case _:
                print("Invalid option")


def call_register_menu():
    while True:
        print("""
CALL REGISTER
1. Missed calls
2. Received calls
3. Dialed numbers
4. Erase lists
5. Show call duration
6. Show call costs
7. Call cost settings
8. Prepaid credit
0. Back
""")

        c = get_int("Enter your choice: ")
        if c is None:
            continue
        if c == 0:
            return

        match c:
            case 5:
                print("Call Duration menu")
            case 6:
                print("Call Costs menu")
            case 7:
                print("Call Cost Settings")
            case _:
                print("Invalid option")


def settings_menu():
    while True:
        print("""
SETTINGS
1. Call settings
2. Phone settings
3. Security settings
4. Restore factory settings
0. Back
""")

        c = get_int("Enter your choice: ")
        if c is None:
            continue
        if c == 0:
            return

        match c:
            case 1:
                print("Call settings menu")
            case 2:
                print("Phone settings menu")
            case 3:
                print("Security settings menu")
            case _:
                print("Invalid option")


# DIRECT START (NO main_menu FUNCTION)
while True:
    print("""
MAIN MENU
1. English
9. Exit
""")

    menu = get_int("Enter your choice: ")

    if menu is None:
        continue

    match menu:
        case 1:
            english_menu()
        case 9:
            print("Exiting program. Goodbye!")
            break
        case _:
            print("Invalid choice.")