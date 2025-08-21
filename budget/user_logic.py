from categoryList import CategoryList
import os
import json

class User:
    def __init__(self, username, password, categories=None):
        self.username = username
        self.password = password
        self.categories = categories if categories is not None else []

    def __str__(self):
        cat_str = "\n    ".join(str(i) for i in self.categories)
        return (f"Username: {self.username} --- Password: {self.password} --- Categories:\n {cat_str if cat_str else 'No categories yet'}")

    # --- File path for this user ---
    @property
    def save_file(self):
        return f"{self.username}_data.json"

    # --- Save/Load Data ----
    def save_data(self):
        with open(self.save_file, "w") as f:
            json.dump([cat.to_dict() for cat in self.categories], f, indent=4)

    def load_data(self):
        if not os.path.exists(self.save_file):
            return []
        with open(self.save_file, "r") as f:
            data = json.load(f)
            return [CategoryList.from_dict(cat) for cat in data]

    def run(self):
        self.categories = self.load_data()

        while True:
            print("\n--- Budget App---")
            print("1. Add new category")
            print("2. Add item to category")
            print("3. Remove item")
            print("4. View categories")
            print("5. Save & Exit")

            choice = input("Choose an option: ")

            if choice == "1":
                title = input("Enter category title: ")
                priority = int(input("Input priority (1 - 5): "))
                total = float(input("Enter total budget allocated: "))
                available = total
                status = "Active"
                items = []
                category = CategoryList(title, priority, total, available, status, items)
                self.categories.append(category)
                print(f"Category --{title}-- created.")

            elif choice == "2":
                if not self.categories:
                    print("No categories found.")
                    continue

                print("Available categories: ")
                for idx, cat in enumerate(self.categories):
                    print(f"{idx + 1}. {cat.title} (Available: {cat.available})")

                try:
                    cat_choice = int(input("Choose category: ")) - 1
                    if 0 <= cat_choice < len(self.categories):
                        subject = input("Enter subject: ")
                        amount = float(input("Enter amount: "))
                        date = input("Enter date: ")
                        self.categories[cat_choice].addItem(subject, amount, date)
                        print("Item added successfully.")
                    else:
                        print("Invalid category choice")
                except ValueError:
                    print("Invalid input, please enter a number")

            elif choice == "3":
                if not self.categories:
                    print("No categories found")
                    continue

                print(f"Available Categories")
                for idx, cat in enumerate(self.categories):
                    print(f"{idx + 1}. {cat.title}")
                
                try:
                    cat_choice = int(input("Choose category: ")) - 1
                    if 0 <= cat_choice < len(self.categories):
                        if not self.categories[cat_choice].items:
                            print("No items found")
                            continue
                        else:
                            for idx, item in enumerate(self.categories[cat_choice].items):
                                print(f"{idx + 1}. {item.subject} ({item.amount} | {item.date})")
                    
                            try:
                                item_choice = int(input("Choose item: ")) - 1
                                if 0 <= item_choice < len(self.categories[cat_choice].items):
                                    self.categories[cat_choice].removeItem(self.categories[cat_choice].items[item_choice])
                                    print("Item removed successfully.")
                                else:
                                    print("Invalid entry.")
                            except ValueError:
                                print("Invalid input, please enter a number")
                    else: 
                        print("Invalid entry.")
                except ValueError:
                    print("Invalid entry. Please enter a number.")

            elif choice == "4":
                if not self.categories:
                    print("No categories found")
                    continue
                for cat in self.categories:
                    print("\n" + str(cat))

            elif choice == "5":
                self.save_data()
                print("Data saved. Goodbye!")
                break
                
            else:
                print("Invalid choice, try again.")

