'''
Homework 3, Excercise 3
Osvaldo Canales
February 22, 2023
Modify a dictionary with an inventory list that counts the totals for each

'''

#Dictionary that stores the name as the key and the number of items as the value
storeInventory = {
    "Hand sanitizer": 10,
    "Soap": 6,
    "Kleenex": 22,
    "Lotion": 16,
    "Razors": 12
}

#function that will dislay the inventory in nice format
def printInventory(inventory):
    print("Inventory:")
    print("----------")
    for item, quantity in inventory.items():
        print(f"{item}: {quantity}")
    print("----------")

#Function that will add a new item or add to existing item
def addItem(inventory, item):
    if item in inventory:
        inventory[item] += 1
    else:
        inventory[item] = 1

#Function that will delete an item, but will not delete the item group
def deleteItem(inventory, item):
    if item not in inventory:
        print(f"Error: {item} does not exist in the inventory.")
    elif inventory[item] == 0:
        print(f"Error: {item} count is already 0, cannot be deleted any further.")
    else:
        inventory[item] -= 1

#Example of item called "Gum" added into the inventory
addItem(storeInventory,'Gum')

#Example of an additional soap added in
addItem(storeInventory,'Soap')

#Example of a razor being deleted 
deleteItem(storeInventory,'Razors')

#Call the function with given inventory 
printInventory(storeInventory)