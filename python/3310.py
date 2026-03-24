print("""
        MAIN MENU
      Please select a language:
        1. English
        2. Yoruba
        3. Hausa
        4. Igbo
        9. Exit
""")

menu = int(input("Enter your choice: "))

match menu:
    case 1:
        # Main English Menu
        print("""
Welcome to the 3310 phone program
Please select an option:
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
""")
        main_option = int(input("Enter your choice: "))

        match main_option:
            case 1:  # PhoneBook
                print("""
You selected PhoneBook
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
""")
                phonebook_choice = int(input("Enter your choice: "))
                match phonebook_choice:
                    case 8:
                        print("You selected Options\n1. Type of view\n2. Memory status")
            case 2:  # Messages
                print("""
You selected Messages
1. Write messages
2. Inbox
3. Outbox
4. Picture messages
5. Templates
6. Smileys
7. Message settings
8. Info service
9. Voice mailbox number
10. Service command editor
""")
                messages_choice = int(input("Enter your choice: "))
                match messages_choice:
                    case 7:
                        print("You selected Message settings\n1. Set 1\n2. Common")
            case 3:
                print("You selected Chat")
            case 4:  # Call register
                print("""
You selected Call register
1. Missed calls
2. Received calls
3. Dialed numbers
4. Erase recent call lists
5. Show call duration
6. Show call costs
7. Call cost settings
8. Prepaid credit
""")
                call_choice = int(input("Enter your choice: "))
                match call_choice:
                    case 5:
                        print("""
You selected Show Call Duration
1. Last call duration
2. All calls' duration
3. Received calls' duration
4. Dialed calls' duration
5. Clear timers
""")
                    case 6:
                        print("""
You selected Show Call Costs
1. Last Call cost
2. All Calls Cost
3. Clear Counter
""")
                    case 7:
                        print("""
You selected Call Cost Settings
1. Call cost Limit
2. Show Costs in
""")
            case 5:  # Tones
                print("""
You selected Tones
1. Ringing tone
2. Ringing volume
3. Incoming call alert
4. Composer
5. Message alert tone
6. Keypad tones
7. Warning and game tones
8. Vibrating alert
9. Screen saver
""")
            case 6:  # Settings
                print("""
You selected Settings
1. Call settings
2. Phone settings
3. Security settings
4. Restore factory settings
""")
                settings_choice = int(input("Enter your choice: "))
                match settings_choice:
                    case 1:
                        print("""
You selected Call settings
1. Automatic redial
2. Speed dialing
3. Call waiting options
4. Own number sending
5. Phone line in use
6. Automatic answer
""")
                    case 2:
                        print("""
You selected Phone settings
1. Language
2. Call info display
3. Welcome note
4. Network selection
5. Lights
6. Confirm SIM service actions
""")
                    case 3:
                        print("""
You selected Security settings
1. PIN code request
2. Call barring service
3. Fixed dialing
4. Closed user group
5. Phone security
6. Change access codes
""")
            case 7:
                print("You selected Call divert")
            case 8:
                print("You selected Games")
            case 9:
                print("You selected Calculator")
            case 10:
                print("You selected Reminders")
            case 11:
                print("""
You selected Clock
1. Alarm clock
2. Clock settings
3. Date settings
4. Stopwatch
5. Countdown timer
6. Auto update of date and time
""")
            case 12:
                print("You selected Profiles")
            case 13:
                print("You selected SIM services")
    case 2:
        print("""Kaabo si eto foonu 3310
              Jowo yan aṣayan kan:
              1. Iwe foonu
              2. Awọn ifiranṣẹ
              3. Iwiregbe
              4. Ipe iforukọsilẹ
              5. Awọn ohun
              6. Eto
              7. Ipe divert
              8. Awọn ere
              9. Kọmputa
              10. Awọn ikilọ
              11. Aago
              12. Awọn profaili
              13. Awọn iṣẹ SIM""")
        options = int(input("Enter your choice: "))
        match options:
             case 1: print("""You selected Iwe foonu
                                         Please select an option:
                                         1. Search
                                         2. Service Nos.
                                         3. Add name
                                         4. Erase
                                         5. Edit
                                         6. Assign tone
                                         7. Send b'card
                                         8. Options
                                         9. Speed dials
                                         10. Voice tags""")
             case 2: print("""You selected Awọn ifiranṣẹ
                                         please select an option:
                                         1. Write messages
                                         2. Inbox  
                                         3. Outbox
                                         4. Picture messages
                                         5. Templates
                                         6. Smileys
                                         7. Message settings
                                         8. Info service
                                         9. Voice mailbox number
                                         10. Service command editor""")
             case 3: print("You selected Iwiregbe")
             case 4: print("""You selected Ipe iforukọsilẹ
                                         Please select an option:
                                         1. Missed calls
                                         2. Received calls
                                         3. Dialed numbers
                                         4. Erase recent call lists
                                         5. Show call duration
                                         6. Show call costs
                                         7. Call cost settings
                                         8. Prepaid credit""")
             case 5: print("""You selected Awọn ohun
                                         Please select an option:
                                         1. Ringing tone
                                         2. Ringing volume
                                         3. Incoming call alert
                                         4. Composer
                                         5. Message alert tone
                                         6. Keypad tones
                                         7. Warning and game tones
                                         8. Vibrating alert
                                         9. Screen saver""")
             case 6: print("""You selected Eto
                                         Please select an option:
                                         1. Call settings
                                         2. Phone settings  
                                         3. Security settings
                                         4. Restore factory settings""")
             case 7: print("You selected Ipe divert")
             case 8: print("You selected Awọn ere")
             case 9: print("You selected Kọmputa")
             case 10: print("You selected Awọn ikilọ")
             case 11: print("""You selected Aago
                                         Please select an option:
                                         1. Alarm clock
                                         2. Clock settings
                                         3. Date settings
                                         4. Stopwatch
                                         5. Countdown timer
                                         6. Auto update of date and time""")
             case 12: print("You selected Awọn profaili")
             case 13: print("You selected Awọn iṣẹ SIM")
    case 3:
        print("""Barka da zuwa shirin wayar 3310
              Don Allah zaɓi zaɓi:
              1. Littafin waya
              2. Saƙonni
              3. Chat
              4. Rijistar kira
              5. Tones
              6. Saituna
              7. Kira divert
              8. Wasanni
              9. Calculator
              10. Tunatarwa
              11. Agogo
              12. Profiles
              13. Ayyukan SIM""")
        options = int(input("Enter your choice: "))
        match options:
             case 1: print("""You selected Littafin waya
                                         Please select an option:
                                         1. Search
                                         2. Service Nos.
                                         3. Add name
                                         4. Erase
                                         5. Edit
                                         6. Assign tone
                                         7. Send b'card
                                         8. Options
                                         9. Speed dials
                                         10. Voice tags""")
             case 2: print("""You selected Saƙonni
                                         Please select an option:
                                         1. Write messages
                                         2. Inbox
                                         3. Outbox
                                         4. Picture messages
                                         5. Templates
                                         6. Smileys
                                         7. Message settings
                                         8. Info service
                                         9. Voice mailbox number 
                                         10. Service command editor""")
             case 3: print("You selected Chat")
             case 4: print("""You selected Rijistar kira
                                         Please select an option:
                                         1. Missed calls
                                         2. Received calls
                                         3. Dialed numbers
                                         4. Erase recent call lists
                                         5. Show call duration
                                         6. Show call costs
                                         7. Call cost settings
                                         8. Prepaid credit""")
             case 5: print("""You selected Tones
                                         Please select an option:
                                          1. Ringing tone
                                         2. Ringing volume
                                         3. Incoming call alert
                                         4. Composer
                                         5. Message alert tone
                                         6. Keypad tones
                                         7. Warning and game tones
                                         8. Vibrating alert
                                         9. Screen saver""")
             case 6: print("""You selected Saituna
                                         Please select an option:
                                           1. Call settings
                                         2. Phone settings
                                         3. Security settings
                                         4. Restore factory settings
                                         """)
             case 7: print("You selected Kira divert")
             case 8: print("You selected Wasanni")
             case 9: print("You selected Calculator")
             case 10: print("You selected Tunatarwa")
             case 11: print("""You selected Agogo
                                         Please select an option:
                                         1. Alarm clock
                                         2. Clock settings
                                         3. Date settings
                                         4. Stopwatch
                                         5. Countdown timer
                                         6. Auto update of date and time""")
             case 12: print("You selected Profiles")
             case 13: print("You selected Ayyukan SIM")

    case 4:
        print("""Ndewo na sistemụ ekwentị 3310
              Biko họrọ nhọrọ:
              1. Akwụkwọ ekwentị
              2. Ozi
              3. Chat
              4. Ndebanye aha oku
              5. Tones
              6. Ntọala
              7. Kpọọ divert
              8. Egwuregwu
              9. Calculator
              10. Ncheta
              11. Elekere
              12. Profiles
              13. SIM ọrụ""")
        options = int(input("Enter your choice: "))
        match options:
             case 1: print("""You selected Akwụkwọ ekwentị
                                         Please select an option:
                                         1. Search
                                         2. Service Nos.
                                         3. Add name
                                         4. Erase
                                         5. Edit
                                         6. Assign tone
                                         7. Send b'card
                                         8. Options
                                         9. Speed dials
                                         10. Voice tags""")
             case 2: print("""You selected Ozi
                                         please select an option:
                                         1. Write messages
                                         2. Inbox
                                         3. Outbox
                                         4. Picture messages
                                         5. Templates
                                         6. Smileys
                                         7. Message settings
                                         8. Info service
                                         9. Voice mailbox number
                                         10. Service command editor""")
             case 3: print("You selected Chat")
             case 4: print("You selected Ndebanye aha oku")
             case 5: print("""You selected Tones
                                         Please select an option:
                                         1. Ringing tone
                                         2. Ringing volume
                                         3. Incoming call alert
                                         4. Composer
                                         5. Message alert tone
                                         6. Keypad tones
                                         7. Warning and game tones
                                         8. Vibrating alert
                                         9. Screen saver""")
             case 6: print("""You selected Ntọala
                                         1. call settings
                                         2. Phone settings
                                         3. Security settings
                                         4. Restore factory settings""")
             case 7: print("You selected Kpọọ divert")
             case 8: print("You selected Egwuregwu")
             case 9: print("You selected Calculator")
             case 10: print("You selected Ncheta")
             case 11: print("""You selected Elekere
                                         Please select an option:
                                         1. Alarm clock
                                         2. Clock settings
                                         3. Date settings
                                         4. Stopwatch
                                         5. Countdown timer
                                         6. Auto update of date and time""")
             case 12: print("You selected Profiles")
             case 13: print("You selected SIM ọrụ")

    case 9:
        print("Exiting program. Goodbye!")
    case _:
        print("Invalid choice. Please select a valid option.")