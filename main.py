game_library = {
    "Donkey Kong": {"copies_available": 3, "cost": 2},
    "Super Mario Bros": {"copies_available": 5, "cost": 3},
    "Tetris": {"copies_available": 2, "cost": 1}
}

acc_lib = {}

def Avail_games():
    print("Available Games:")
    for index, (game_title, game_info) in enumerate(game_library.items(), start=1):
        print(f"{index}. {game_title} - Copies available: {game_info['copies_available']}, Cost: ${game_info['cost']}")

def register():
    while True:
        try:
            print("REGISTER PAGE")
            print("Please input information")
            username = input("Please input username: ")
            password = input("Password (must be 8 characters long): ")
            if len(password) >= 8:
                print("Account registered successfully")
                userbalance = 0
                userpoints = 0

                acc_lib[username] = {
                    "username": username,
                    "password": password,
                    "Balance": userbalance,
                    "Points": userpoints,
                    "inventory": []
                }
                menu()
            else:
                print("Password must be at least 8 characters long")
                break
        except ValueError:
            print("Wrong input")
            input()
            return

def userlogin():
    while True:
        try:
            print("LOGIN PAGE")
            username = input("Username: ")
            password = input("Password: ")
            if username in acc_lib and acc_lib[username]["password"] == password:
                print("Login Successful")
                user_menu(username)
            else:
                print("Invalid username or password")
                break
        except ValueError:
            print("Wrong input")
            input()
            return

def adminlogin():
    while True:
        try:
            print("ADMIN LOGIN PAGE")
            admin = str(input("Username: "))
            if admin == "admin":
                adminpass = str(input("Password: "))
                if adminpass == "adminpass":
                    print("Login Successful")
                    admin_menu()
                else:
                    print("Incorrect password")
            else:
                print("Incorrect Username")
                break
        except ValueError:
            print("Wrong input")
            input()
            return

def user_menu(username):
    while True:
        try:
            print(f"Logged in as {username}")
            print("1. Rent a game")
            print("2. Return a game")
            print("3. Top-up Account")
            print("4. Display inventory")
            print("5. Redeem free game rental")
            print("6. Check Points")
            print("7. Log out")

            choice = input("Enter your choice: ")

            if choice == "1":
                rent_game(username)
            elif choice == "2":
                return_game(username)
            elif choice == "3":
                top_up(username)
            elif choice == "4":
                inventory(username)
            elif choice == "5":
                redeem(username)
            elif choice == "6":
                check_point(username)
            elif choice == "7":
                print("Logging out...Goodbye!")
                menu()
                break
            else:
                print("Please input a valid option")
        except ValueError:
            print("Wrong input")
            return

def admin_menu():
    while True:
        try:
            print("Admin Menu") 
            print("1. Update Game Details")
            print("2. Log out")
            
            choice = input("Enter your choice: ")
            
            if choice == "1":
                update_menu()
            elif choice == "2":
                print("Logging out...Goodbye!")
                menu()
                break
            else:
                print("Please input a valid option")
        except ValueError:
            print("Wrong input")
            return

def update_menu():
    while True:
        try:
            print("Update Game ")
            print("1. Update Game Copies")
            print("2. Update Game Cost")
            print("3. Back to Menu")
            
            choice = input("Enter your choice: ")
            
            if choice == "1":
                update_game_copies()
            elif choice == "2":
                update_game_cost()
            elif choice == "3":
                admin_menu()
                break
            else:
                print("Please input a valid option")
        except ValueError:
            print("Wrong input")
            return

def update_game_copies():
    Avail_games()
    game_choice = input("Select a game to update copies: ")
    game_choice = int(game_choice)
    if game_choice in range(1, len(game_library) + 1):
        game_name = list(game_library.keys())[game_choice - 1]
        new_copies = int(input(f"Enter new number of copies for {game_name}: "))
        game_library[game_name]["copies_available"] = new_copies
        print(f"{game_name} copies updated successfully.")
    else:
        print("Invalid game choice.")

def update_game_cost():
    Avail_games()
    game_choice = input("Select a game to update cost: ")
    game_choice = int(game_choice)
    if game_choice in range(1, len(game_library) + 1):
        game_name = list(game_library.keys())[game_choice - 1]
        new_cost = int(input(f"Enter new cost for {game_name}: "))
        game_library[game_name]["cost"] = new_cost
        print(f"{game_name} cost updated successfully.")
    else:
        print("Invalid game choice.")

def top_up(username):
    while True:
        try:
            amount = float(input("Enter the amount you want to top up: $"))
            if amount > 0:
                acc_lib[username]["Balance"] += amount
                print(f"Top-up successful. New balance: ${acc_lib[username]['Balance']}")
                break
            else:
                print("Please enter a positive amount to top up.")
        except ValueError:
            print("Invalid input. Please enter a valid amount.")

def rent_game(username):
    Avail_games()
    game_choice = input("Please select a game to rent: ")
    game_choice = int(game_choice)
    if game_choice in range(1, len(game_library) + 1):
        game_name = list(game_library.keys())[game_choice - 1]
        if game_library[game_name]["copies_available"] > 0:
            game_cost = game_library[game_name]["cost"]
            if acc_lib[username]["Balance"] >= game_cost:
                print(f"{game_name} rented successfully.")
                game_library[game_name]["copies_available"] -= 1
                acc_lib[username]["inventory"].append(game_name)
                acc_lib[username]["Balance"] -= game_cost
                acc_lib[username]["Points"] += int(game_cost / 2)  # Update points
                return
            else:
                print("Insufficient balance. Please top up your account to rent this game.")
        else:
            print("Sorry, no copies available for renting.")
            return
    else:
        print("Invalid game choice.")
        return

def inventory(username):
    print(f"Inventory for {username}:")
    for game in acc_lib[username]["inventory"]:
        print(game)

def redeem(username):
    points_needed = 3
    if acc_lib[username]["Points"] >= points_needed:
        free_games = acc_lib[username]["Points"] // points_needed
        print(f"Congratulations! You can redeem {free_games} free game(s).")
        acc_lib[username]["Points"] -= free_games * points_needed
        for _ in range(free_games):
            # Add free game(s) to inventory
            print("Free game redeemed.")
    else:
        print("Not enough points to redeem a free game.")

def check_point(username):
    print(f"Points for {username}: {acc_lib[username]['Points']}")

def return_game(username):
    print("Inventory:")
    inventory(username)
    
    if not acc_lib[username]["inventory"]:
        print("No games to return.")
    else:
        print("Select a game to return:")
        for index, game in enumerate(acc_lib[username]["inventory"], start=1):
            print(f"{index}. {game}")
        
        game_choice = input("Enter the number of the game to return: ")
        game_choice = int(game_choice)
        if game_choice in range(1, len(acc_lib[username]["inventory"]) + 1):
            game_to_return = acc_lib[username]["inventory"][game_choice - 1]
            game_library[game_to_return]["copies_available"] += 1
            acc_lib[username]["inventory"].remove(game_to_return)
            print(f"{game_to_return} returned successfully.")
        else:
            print("Invalid game choice.")

def menu():
    while True:
        try:
            print("Welcome to the Game Rental System")
            print("1. Display Available Games")
            print("2. Register User")
            print("3. Log in")
            print("4. Admin Log in")
            print("5. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                Avail_games()
            elif choice == "2":
                register()
            elif choice == "3":
                userlogin()
            elif choice == "4":
                adminlogin()
            elif choice == "5":
                print("Closing app...Goodbye!")
                return
            else:
                print("Please input a valid option")
        except ValueError:
            print("Wrong input")
            return

menu()