#  ----------------items player currently has----------
items = {'Arrow': 12, 'Bow': 1, 'Rifle': 2, 'Pistol': 5, 'Gold coin': 42}

#  ----------------items found in the loot stash------------
dragonLoot = ['Gold coin', 'Bow', 'Gold coin', 'Pistol', 'Arrow', 'Bomb', 'Arrow', 'Pistol']

#  -------------------fucntion to traverse through the item and display total item-------


def displayinventory(inventory):
    print('Inventory and items')
    item_total = 0
    for k, v in inventory.items():  # to display both key and values
        print(k + ' : ' + str(v))
        item_total += v
    print("Total number of items now: " + str(item_total))

#  -----------fucntion to add items in the loot stash to items----------------


def addtoinventory(inventory, more_items):
    for i in more_items:
        if i in inventory.keys():
            inventory[i] += 1
        else:
            inventory.setdefault(i, 1)

    return inventory


addtoinventory(items, dragonLoot)  # ---------updating items
displayinventory(items)  # ---------call to fucntion to display the inventory

# displayinventory(items)
