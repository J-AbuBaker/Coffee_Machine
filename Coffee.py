class Coffee:
    @classmethod
    def has_enough_resources(cls, owner, water, coffee_beans, milk=0, vanilla_syrup=0, caramel_syrup=0, chocolate_syrup=0):
        inventory = owner.load_inventory()
        return (
            inventory['water'] >= water and
            inventory['coffee_beans'] >= coffee_beans and
            inventory['milk'] >= milk and
            inventory['vanilla_syrup'] >= vanilla_syrup and
            inventory['caramel_syrup'] >= caramel_syrup and
            inventory['chocolate_syrup'] >= chocolate_syrup and
            inventory['cups'] >= 1
        )

    @classmethod
    def deduct_resources(cls, owner, water, coffee_beans, milk=0, vanilla_syrup=0, caramel_syrup=0, chocolate_syrup=0):
        inventory = owner.load_inventory()
        inventory['water'] -= water
        inventory['coffee_beans'] -= coffee_beans
        inventory['milk'] -= milk
        inventory['vanilla_syrup'] -= vanilla_syrup
        inventory['caramel_syrup'] -= caramel_syrup
        inventory['chocolate_syrup'] -= chocolate_syrup
        inventory['cups'] -= 1
        owner.save_inventory(inventory)

    @classmethod
    def add_cash(cls, owner, amount):
        owner.cash_balance += amount
