from agent.vars.actions import BUY, SELL, NOTHING

class Market:
    """
    Represents a market containing various items.
    """

    def __init__(self, items):
        """
        Initializes a new market instance with a list of items.
        """
        self.inventory = {}
        self.ALLOWED_ACTIONS = {BUY, SELL, NOTHING}

        print('\n[INFO] Created Market:')
        print('[INFO] Adding items...')
        for item in items:
            self.add_item(item)
            print(f'[INFO] ---> Added item {item.id}: {item}')

    ####
    ## Class decorators
    ####

    # Decorator to check if the item is in inventory
    def __isItemInInventory(func):
        """
        Decorator to check if the item exists in the inventory before performing an action.
        """
        def wrapper(self, item, *args, **kwargs):
            if item not in self.inventory:
                raise Exception(f'[ERROR] {item.id} does not exist in inventory')
            return func(self, item, *args, **kwargs)
        return wrapper


    ####
    ## Class public methods
    ####

    ### Default methods
    #####

    def add_item(self, item):
        """
        Adds a new item to the market inventory.
        """
        if item.id in self.inventory:
            raise Exception(f'[ERROR] {item.id} "{item.name}" already exists, it must be updated')
        
        self.inventory[item.id] = item
        print(f'[INFO] Created "{item.id}" item')
        print(f'[INFO] --> {item}')
        return self.inventory[item.id]

    @__isItemInInventory
    def get_item(self, id):
        """
        Retrieves an item from the market inventory by its id.
        """
        print(f'[INFO] Getting "{id}" item')
        print(f'[INFO] --> {self.inventory[id]}')
        return self.inventory[id]

    @__isItemInInventory
    def update_item(self, id, **attributes):
        """
        Updates attributes of an item in the market inventory.
        """
        for attribute, value in attributes.items():
            self.inventory[id][attribute] = value
        print(f'[INFO] Updated "{id}" item')
        print(f'[INFO] --> {self.inventory[id]}')
        return self.inventory[id]

    @__isItemInInventory
    def delete_item(self, id):
        """
        Deletes an item from the market inventory by its id.
        """
        del self.inventory[id]
        print(f'[INFO] Deleted "{id}" item')
        return True
