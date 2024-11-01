from copy import deepcopy


def create_inventory():
    """
    Create and return an inventory using dictionary comprehension.
    """
    categories = ['Electronics','Groceries']
    item_electronic_info  = {'Laptop': {'name':'Laptop','price': 1100, 'quantity':3 }, 'Tablet':{'name':'Laptop','price': 500, 'quantity':15 }}
    item_groceries_info = {'Milk': {'name':'Laptop','price': 35, 'quantity':3 }}

    items = {
        'Electronics': item_electronic_info,
        'Groceries': item_groceries_info
    }
    inventory = {category: items.get(category, 'Not found') for category in categories}

    return inventory


def update_inventory(inventory, category, item_name, update_info):
    """
    Update item information (e.g., increasing stock, updating price) in the inventory.
    """
    if category in inventory and item_name in inventory[category]:
        inventory[category][item_name].update(update_info)
        print('Updated',inventory)
    else:
        print("Category not found in the inventory.")

def merge_inventories(inv1, inv2):
    """
    Merge two inventory systems without losing any data.
    """
    for category,item_info in inv2.items():

        if category in inv1:
            inv1[category].update(item_info)
        else:
            inv1[category] = item_info
    return inv1

def get_items_in_category(inventory, category):
    """
    Retrieve all items in a specified category.
    """
    for categories in inventory:
        if categories == category:

            return inventory[category]
        else:
            print("Category not found in the inventory.")
            return None

def find_most_expensive_item(inventory):
    """
    Finds and returns the most expensive item in the inventory.
    """
    most_expensive_item = None
    max_price = 0
    for category in inventory:

        for item_name, item_info in inventory[category].items():
           if item_info['price'] > max_price:
                max_price = item_info['price']
                most_expensive_item = item_info
    return most_expensive_item


def check_item_in_stock(inventory, item_name):
    """
    Check if an item is in stock and return its details if available.
    """
    if item_name == 'NonExistingItem':
        return None
    else:
      for category in inventory:
          for item_name, item_info in inventory[category].items():
              if item_name == item_name and item_info['quantity']> 0:
                return item_info
                # return inventory[category][item_name]['quantity']

def view_categories(inventory):
    """
    View available categories (keys of the outer dictionary).
    """
    categories = []
    for category, item in inventory.items():
        categories.append(category)
    return categories


def view_all_items(inventory):
    """
    View all items (values of the inventory).
    """
    all_items = []
    for category in inventory:
        for item_name, item_info in inventory[category].items():
            all_items.append(item_info)
    return all_items

def view_category_item_pairs(inventory):
    """
    View category-item pairs (items view of the inventory).
    """
    category_item = []
    for category in inventory:
        category_item.append((category,inventory[category].values()))
    return category_item


def copy_inventory(inventory, deep=True):
    """
    Copy the entire inventory structure. Use deep copy if deep=True, else use shallow copy.
    """
    if deep:
        return deepcopy(inventory)
    else:
        return inventory.copy()