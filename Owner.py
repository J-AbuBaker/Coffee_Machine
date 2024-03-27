import csv
from tabulate import tabulate
from colorama import Fore, Style


class Owner:
    USERNAME = 'user'
    PASSWORD = 'password'
    FIELDS = ['water', 'coffee_beans', 'milk', 'vanilla_syrup',
                'caramel_syrup', 'chocolate_syrup', 'cups']


    def __init__(self, username, password, inventory_file, cash_balance=0.0):
        self.username = username
        self.password = password
        self.inventory_file = inventory_file
        self.cash_balance = cash_balance
        self.inventory = self.load_inventory()

    def load_inventory(self):
        inventory = {}
        try:
            with open(self.inventory_file, 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    for field in Owner.FIELDS:
                        inventory[field] = int(row[field])
        except FileNotFoundError:
            print('Inventory file not found.\nCreating a new one...')
            inventory = {field: 0 for field in Owner.FIELDS}
            print(self.save_inventory(inventory))
            print('New inventory file created successfully.\n')
        return inventory

    def save_inventory(self, inventory):
        with open(self.inventory_file, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=Owner.FIELDS)
            writer.writeheader()
            writer.writerow(inventory)
        return 'Inventory saved successfully.\n'

    def add_ingredients(self):
        inventory = {}
        for field in Owner.FIELDS:
            if field in ['water', 'milk', 'vanilla_syrup', 'caramel_syrup', 'chocolate_syrup']:
                unit = 'ml'
            elif field == 'coffee_beans':
                unit = 'gm'
            else:
                unit = ''

            quantity = input(f'Enter quantity of {field} ({unit}): ')
            try:
                inventory[field] = int(quantity)
            except ValueError:
                print(
                    f"Invalid quantity for {field}. Please enter a valid integer.")
                return self.add_ingredients()

        self.save_inventory(inventory)
        print("Ingredients added successfully.\n")

    def withdraw_ingredient(self):
        inventory = self.load_inventory()
        for ingredient, quantity in inventory.items():
            withdraw_quantity = int(
                input(f'Enter quantity of {ingredient} to withdraw: '))
            if withdraw_quantity <= quantity:
                inventory[ingredient] -= withdraw_quantity
            else:
                print(f"Not enough {ingredient} quantity in inventory.")
        self.save_inventory(inventory)
        print("Ingredients withdrawn successfully.\n")

    def add_cash(self, amount):
        self.cash_balance += amount
        print(f"${amount} added to cash balance.")
        print(f"Current balance: ${self.cash_balance}\n")

    def withdraw_cash(self, amount):
        if self.cash_balance >= amount:
            self.cash_balance -= amount
            print(f"${amount} withdrawn from cash balance.")
            print(f"Current balance: ${self.cash_balance}\n")
        else:
            print("Insufficient funds.\n")

    def display_inventory(self):
        inventory = self.load_inventory()
        inventory_data = []
        for ingredient, quantity in inventory.items():
            unit = ''
            if ingredient in ['water', 'milk', 'vanilla_syrup', 'caramel_syrup', 'chocolate_syrup']:
                unit = 'ml'
            elif ingredient == 'coffee_beans':
                unit = 'gm'
            inventory_data.append((ingredient, f'{quantity} {unit}'))
        print(tabulate(inventory_data, headers=[
                'Ingredient', 'Quantity'], tablefmt='github'))
        print()

    def authenticate(self, username, password):

        if self.username == Owner.USERNAME and self.password == Owner.PASSWORD:
            return True, ""
        elif self.username != Owner.USERNAME:
            return False, "Username does not match."
        else:
            return False, "Password is incorrect."

    def display_menu(self):
        menu_options = [
            (1, 'Add Ingredients'),
            (2, 'Withdraw Ingredients'),
            (3, 'Display Ingredients'),
            (4, 'Add Cash'),
            (5, 'Withdraw Cash'),
            (6, 'Display Cash'),
            (7, 'Exit Menu')
        ]
        auth_result, auth_message = self.authenticate(
            self.username, self.password)

        if auth_result:
            print()
            print(Fore.GREEN +
                    f"Welcome {self.username}! Authentication successful.")
            print(Fore.GREEN + "Access granted to the menu.\n")
            print(Style.RESET_ALL)
            print(tabulate(menu_options, headers=[
                    'Option', 'Description'], tablefmt='grid'))

            while True:
                try:
                    option = int(input('Please select an option (1-7): '))
                    if option not in range(1, 8):
                        print(
                            'Invalid option. Please select a number between 1 and 7.\n')
                    else:
                        print()
                        if option == 1:
                            print("Adding ingredients...\n")
                            self.add_ingredients()
                        elif option == 2:
                            print("Withdrawing ingredients...\n")
                            self.withdraw_ingredient()
                        elif option == 3:
                            print("Displaying Ingredients...\n")
                            self.display_inventory()
                        elif option == 4:
                            amount = float(input('Enter the amount to add: '))
                            print("Adding cash...\n")
                            self.add_cash(amount)
                        elif option == 5:
                            amount = float(
                                input('Enter the amount to withdraw: '))
                            print("Withdrawing cash...\n")
                            self.withdraw_cash(amount)
                        elif option == 6:
                            print("Displaying Cash...\n")
                            print(f'Your current cash balance is: ${self.cash_balance}\n')
                        elif option == 7:
                            return
                except ValueError:
                    print('Invalid input. Please enter a valid number.\n')
        else:
            print(Fore.RED + f"Authentication failed: {auth_message}")
            print(Style.RESET_ALL)



def main():
    owner = Owner('user', 'password', 'inventory.csv', 1000)
    owner.display_menu()


if __name__ == '__main__':
    main()
