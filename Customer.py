from Espresso import Espresso
from Latte import Latte
from Americano import Americano
from Mocha import Mocha
from Owner import Owner
from tabulate import tabulate
import sys


class Customer:

    @classmethod
    def display_coffee_menu(cls):
        menu_options = [
            (1, 'Espresso'),
            (2, 'Latte'),
            (3, 'Americano'),
            (4, 'Mocha'),
        ]
        print()
        print("Coffee Menu".center(30))
        print(tabulate(menu_options, headers=[
                'Option', 'Description'], tablefmt='orgtbl'))

    @classmethod
    def select_coffee(cls):
        while True:
            cls.display_coffee_menu()
            choice = int(input("\nPlease select your coffee (1-4): "))
            if choice == 5:
                sys.exit('Goodbye!')
            elif choice in range(1, 5):
                return choice
            else:
                print("Invalid choice. Please select a number from 1 to 5.")

    @classmethod
    def make_coffee(cls, owner, choice):
        print()
        if choice == 1:
            shot_size = input('single or double shot: ')
            Espresso.make(owner, shot_size)
            print()  # newline print

        elif choice == 2:
            syrup_type = input('vanilla or caramel syrup: ')
            Latte.make(owner, syrup_type)
            print()  # newline print

        elif choice == 3:
            size = input('regular or grande size: ')
            Americano.make(owner, size)
            print()  # newline print

        elif choice == 4:
            chocolate_type = input('dark or white chocolate: ')
            Mocha.make(owner, chocolate_type)
            print()  # newline print


def main():
    owner = Owner('user', 'password', 'inventory.csv', 1000)
    option = Customer.select_coffee()
    Customer.make_coffee(owner, option)


if __name__ == '__main__':
    main()
