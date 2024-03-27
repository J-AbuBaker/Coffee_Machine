from Coffee import Coffee


class Americano(Coffee):
    REGULAR_WATER = 120
    REGULAR_COFFEE_BEANS = 20
    REGULAR_PRICE = 2.50

    GRANDE_WATER = 180
    GRANDE_COFFEE_BEANS = 30
    GRANDE_PRICE = 3.00

    @classmethod
    def make(cls, owner, size):
        size = size.lower().strip()
        if size == 'regular':
            if super().has_enough_resources(owner, cls.REGULAR_WATER, cls.REGULAR_COFFEE_BEANS):
                super().deduct_resources(owner, cls.REGULAR_WATER, cls.REGULAR_COFFEE_BEANS)
                super().add_cash(owner, cls.REGULAR_PRICE)
                print('Regular Americano is ready!')
            else:
                print('Sorry, Not enough resources to make a regular Americano')
        elif size == 'grande':
            if super().has_enough_resources(owner, cls.GRANDE_WATER, cls.GRANDE_COFFEE_BEANS):
                super().deduct_resources(owner, cls.GRANDE_WATER, cls.GRANDE_COFFEE_BEANS)
                super().add_cash(owner, cls.GRANDE_PRICE)
                print('Grande Americano is ready!')
            else:
                print('Sorry, Not enough resources to make a grande Americano')
        else:
            print("Invalid size. Please choose 'regular' or 'grande'.")
