from Coffee import Coffee


class Mocha(Coffee):
    DARK_CHOCOLATE_WATER = 80
    DARK_CHOCOLATE_MILK = 50
    DARK_CHOCOLATE_CHOCOLATE_SYRUP = 40
    DARK_CHOCOLATE_COFFEE_BEANS = 20
    DARK_CHOCOLATE_PRICE = 5.50

    WHITE_CHOCOLATE_WATER = 80
    WHITE_CHOCOLATE_MILK = 50
    WHITE_CHOCOLATE_CHOCOLATE_SYRUP = 20
    WHITE_CHOCOLATE_COFFEE_BEANS = 20
    WHITE_CHOCOLATE_PRICE = 5.00

    @classmethod
    def make(cls, owner, chocolate_type):
        chocolate_type = chocolate_type.lower().strip()
        if chocolate_type == 'dark':
            if super().has_enough_resources(owner, cls.DARK_CHOCOLATE_WATER, cls.DARK_CHOCOLATE_COFFEE_BEANS,
                                            cls.DARK_CHOCOLATE_MILK, chocolate_syrup=cls.DARK_CHOCOLATE_CHOCOLATE_SYRUP):
                super().deduct_resources(owner, cls.DARK_CHOCOLATE_WATER, cls.DARK_CHOCOLATE_COFFEE_BEANS,
                                            cls.DARK_CHOCOLATE_MILK,                                       chocolate_syrup=cls.DARK_CHOCOLATE_CHOCOLATE_SYRUP)
                super().add_cash(owner, cls.DARK_CHOCOLATE_PRICE)
                print('Dark Chocolate Mocha is ready!')
            else:
                print('Sorry, Not enough resources to make a Dark Chocolate Mocha')
        elif chocolate_type == 'white':
            if super().has_enough_resources(owner, cls.WHITE_CHOCOLATE_WATER, cls.WHITE_CHOCOLATE_COFFEE_BEANS,
                                            cls.WHITE_CHOCOLATE_MILK, chocolate_syrup=cls.WHITE_CHOCOLATE_CHOCOLATE_SYRUP):
                super().deduct_resources(owner, cls.WHITE_CHOCOLATE_WATER, cls.WHITE_CHOCOLATE_COFFEE_BEANS,
                                         cls.WHITE_CHOCOLATE_MILK, chocolate_syrup=cls.WHITE_CHOCOLATE_CHOCOLATE_SYRUP)
                super().add_cash(owner, cls.WHITE_CHOCOLATE_PRICE)
                print('White Chocolate Mocha is ready!')
            else:
                print('Sorry, Not enough resources to make a White Chocolate Mocha')
        else:
            print("Invalid chocolate type. Please choose 'dark' or 'white'.")
