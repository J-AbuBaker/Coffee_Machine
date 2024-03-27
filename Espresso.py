from Coffee import Coffee


class Espresso(Coffee):
    SINGLE_SHOT_WATER = 30
    SINGLE_SHOT_COFFEE_BEANS = 15
    SINGLE_SHOT_PRICE = 2.50

    DOUBLE_SHOT_WATER = 60
    DOUBLE_SHOT_COFFEE_BEANS = 30
    DOUBLE_SHOT_PRICE = 3.00

    @classmethod
    def make(cls, owner, shot_size):
        shot_size = shot_size.lower().strip()
        if shot_size == 'single':
            if super().has_enough_resources(owner, cls.SINGLE_SHOT_WATER, cls.SINGLE_SHOT_COFFEE_BEANS):
                super().deduct_resources(owner, cls.SINGLE_SHOT_WATER, cls.SINGLE_SHOT_COFFEE_BEANS)
                super().add_cash(owner, cls.SINGLE_SHOT_PRICE)
                print('Espresso shot (single) is ready!')
            else:
                print('Sorry, Not enough resources for single shot')
        elif shot_size == 'double':
            if super().has_enough_resources(owner, cls.DOUBLE_SHOT_WATER, cls.DOUBLE_SHOT_COFFEE_BEANS):
                super().deduct_resources(owner, cls.DOUBLE_SHOT_WATER, cls.DOUBLE_SHOT_COFFEE_BEANS)
                super().add_cash(owner, cls.DOUBLE_SHOT_PRICE)
                print('Espresso shot (double) is ready!')
            else:
                print('Sorry, Not enough resources for double shot')
        else:
            print("Invalid shot size. Please choose 'single' or 'double'.")
