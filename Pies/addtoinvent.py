stuff_i = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

dragonLoot_a = ['rope', 'gold coin', 'dagger', 'gold coin', 'dagger', 'gold coin', 'ruby']

print(stuff_i)


def addToInventory(inventory, addedItems):

    for k, v in inventory.items():

        n = addedItems.count(k)

        inventory[k] = n + v

    inventory.setdefault(k, n)

    print(inventory)


addToInventory(stuff_i, dragonLoot_a)

