#inventory.py

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
  print('Inventory:')
  item_total = 0
  for key, value in inventory.items():
    #will look at the dictionary in tuple-like

    item_total += value #adds the values

    print(value, key) #print
    
  print("Total number of items: " + str(item_total))

#List to Dictionary Function for Fantasy Game Inventory Exercise
def addInventory(inventory, addedItems):
  #fill in

  for dragon_loot_items in addedItems:
    #if item is not in the original dictionary, then add it 
    if dragon_loot_items not in inventory.keys():
      inventory[dragon_loot_items] = 1
    else:
      inventory[dragon_loot_items] += 1

  return inventory
    

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addInventory(inv, dragonLoot)


displayInventory(stuff)
print('-----+-----+-----+')
print("next exercise")
print('-----+-----+-----+')
displayInventory(inv)
