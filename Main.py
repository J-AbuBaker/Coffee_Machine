from OwnerMenu import OwnerMenu
from CustomerMenu import CustomerMenu
from Owner import Owner
from Customer import Customer
import sys


def main():
    owner = None 
    while True:
        print("Select User Type:")
        print("1. Owner")
        print("2. Customer")
        print("3. Exit")
        try:
            user_type = int(input("Please select an option: "))
            if user_type == 1:
                if owner is None:
                    username = input('\nEnter your username: ')
                    password = input('Enter your password: ')
                    inventory_file = input('Please input the CSV file for inventory: ')
                    print()
                    owner = Owner(username, password, inventory_file)
                owner_menu = OwnerMenu(owner)
                owner_menu.display_main_menu()
            elif user_type == 2:
                if owner is None:
                    print("Wait until the Owner opens.\n")
                else:
                    customer = Customer()
                    customer_menu = CustomerMenu(customer, owner)
                    customer_menu.display_main_menu()
            elif user_type == 3:
                sys.exit('Exiting Coffee Machine.')
            else:
                print("Please enter a valid option.")
        except ValueError:
            print("Please enter a number.")


if __name__ == "__main__":
    main()
    