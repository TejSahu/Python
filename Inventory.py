items = {'Arrow': 12, 'Bow': 1, 'Rifle': 2, 'Pistol': 5, 'Gold coin': 42}

dragonLoot = ['Gold coin', 'Bow', 'Gold coin', 'Pistol', 'Arrow']


def displayinventory(inventory):
    print('Inventory and items')
    item_total = 0
    for k, v in inventory.items():  # to display both key and values
        print(k + ' : ' + str(v))
        item_total += v
    print("Total number of items: " + str(item_total))


def addtoinventory(inventory, more_items):
    for k, v in inventory.items():
        if k in more_items:
            inventory[k] += 1
        else:
            inventory.setdefault(k, 1)

    return inventory


items = addtoinventory(items, dragonLoot)
displayinventory(items)
print(items)
# displayinventory(items)
