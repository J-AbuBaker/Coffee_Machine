from Menu import Menu
from Customer import Customer
import sys

class CustomerMenu(Menu):
    def __init__(self, customer, owner):
        self.customer = customer
        self.owner = owner

    def select_menu(self):
        print("Welcome to the Coffee Shop!")
        print("      ( (")
        print("       ) )")
        print("     ........")
        print("     |      |]")
        print("    \\      /")
        print("      `----'")
        while True:
            print('Customer Menu')
            print('1. Place Order')
            print('2. Back to Main Menu')
            print('3. Exit')
            try:
                option = int(input('Please select an option: '))
                if option not in range(1, 4):
                    print('Please enter a valid option number.')
                else:
                    return option
            except ValueError:
                print('Please enter a number.')

    def display_main_menu(self):
        print()
        while True:
            option = self.select_menu()

            if option == 1:
                # Display customer menu options
                coffee_choice = self.customer.select_coffee()
                if coffee_choice is not None:
                    self.customer.make_coffee(self.owner, coffee_choice)
                print()
            elif option == 2:  # Option to return to main menu
                # input("Press Enter to return to the main menu...")
                print()  
                return  # Return to main menu
            elif option == 3:
                sys.exit('Have a nice day')
