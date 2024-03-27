from Menu import Menu
from Owner import Owner

class OwnerMenu(Menu):
    def __init__(self, owner):
        self.owner = owner

    def select_menu(self):
        while True:
            print('Coffee Shop Owner Menu')
            print('1. Access Management')
            print('2. Back to Main Menu')
            try:
                option = int(input('Please select an option: '))
                if option not in range(1, 4):
                    print('Please enter a valid option number.')
                else:
                    return option
            except ValueError:
                print('Please enter a number.')

    def display_main_menu(self):
        while True:
            option = self.select_menu()

            if option == 1:
                # Display owner menu options
                self.owner.display_menu()
                input("Press Enter to return to the shop owner menu...")
                print()  # newline print
            elif option == 2:  # Option to return to main menu
                input("\nPress Enter to return to the main menu...")
                print()  # newline print
                return  # Return to main menu


def main():
    # Create an Owner object
    owner = Owner('user', 'password', 'inventory.csv', 1000)

    # Create an OwnerMenu object
    owner_menu = OwnerMenu(owner)

    # Display the main menu
    owner_menu.display_main_menu()

if __name__ == "__main__":
    main()
