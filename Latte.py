from Coffee import Coffee

class Latte(Coffee):
    
    VANILLA_LATTE_WATER = 100
    VANILLA_LATTE_COFFEE_BEANS = 20
    VANILLA_LATTE_MILK = 70
    VANILLA_LATTE_SYRUP = 25
    VANILLA_LATTE_PRICE = 4

    CARAMEL_LATTE_WATER = 100
    CARAMEL_LATTE_COFFEE_BEANS = 20
    CARAMEL_LATTE_MILK = 70
    CARAMEL_LATTE_SYRUP = 30
    CARAMEL_LATTE_PRICE = 4.5
    
    @classmethod
    def make(cls, owner, syrup_type):
        syrup_type = syrup_type.lower().strip()
        if syrup_type == 'vanilla':
            if super().has_enough_resources(owner, cls.VANILLA_LATTE_WATER, cls.VANILLA_LATTE_COFFEE_BEANS,
                                        cls.VANILLA_LATTE_MILK, cls.VANILLA_LATTE_SYRUP):
                super().deduct_resources(owner, cls.VANILLA_LATTE_WATER, cls.VANILLA_LATTE_COFFEE_BEANS,
                                        cls.VANILLA_LATTE_MILK, cls.VANILLA_LATTE_SYRUP)
                super().add_cash(owner, cls.VANILLA_LATTE_PRICE)
                print("Vanilla latte is ready!")
            else:
                print("Not enough resources to make vanilla latte")
        elif syrup_type == 'caramel':
            if super().has_enough_resources(owner, cls.CARAMEL_LATTE_WATER, cls.CARAMEL_LATTE_COFFEE_BEANS,
                                        cls.CARAMEL_LATTE_MILK, cls.CARAMEL_LATTE_SYRUP):
                super().deduct_resources(owner, cls.CARAMEL_LATTE_WATER, cls.CARAMEL_LATTE_COFFEE_BEANS,
                                        cls.CARAMEL_LATTE_MILK, cls.CARAMEL_LATTE_SYRUP)
                super().add_cash(owner, cls.CARAMEL_LATTE_PRICE)
                print("Caramel latte is ready!")
            else:
                print("Not enough resources to make caramel latte")
        else:
            print("Invalid syrup type")
