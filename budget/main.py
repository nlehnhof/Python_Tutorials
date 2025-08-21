from user_logic import User
from auth import register_user, authenticate_user

def main():
    while True:
        print("\n--- Welcome to Budget App ---")
        print("1. Login")
        print("2. Register")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":  # Login
            username = input("Username: ")
            password = input("Password: ")
            
            if authenticate_user(username, password):
                print(f"✅ Login successful. Welcome {username}!")
                user = User(username, password)
                user.run()
            else:
                print("❌ Invalid username or password.")

        elif choice == "2":  # Register
            username = input("Choose a username: ")
            password = input("Choose a password: ")
            success, message = register_user(username, password)
            print(message)

        elif choice == "3":  # Exit
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()