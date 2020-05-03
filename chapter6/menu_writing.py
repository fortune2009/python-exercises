def display_menu(choice):
    if choice == 'Y' or choice == 'y':
        print()
        choice = input("Input No. for Menu:\
                        1. Messages\
                        2. Contacts\
                        3. Games\
                        4. Setting\
                        5. Media\
                        6. Web\n-> ")

        if choice == "1":
            choice = input("Input No. for :\
                        1. Inbox\
                        2. Draft\
                        3. Outbox\
                        4. Msg Setting\n->")
            if choice == "1":
                print("Inbox\tunread & read msgs")
                inbox = {"090234": "Hello world",
                         "090456": "Hello world",
                         "090678": "Hello world"}
                print(inbox)

        if choice == "2":
            print("Your contacts")

        if choice == "3":
            print("Your Games")

        if choice == "4":
            print("Settings")

        if choice == "5":
            print("Media")

        if choice == "6":
            print("Web")

    return choice


in_take = input("Type Y for Menu: ")
display_menu(in_take)
