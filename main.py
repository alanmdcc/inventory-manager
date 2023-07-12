from functools import reduce

inventory = [{'Name': 'apple', 'Quantity': 20, 'Unit Price': 3.5, 'Location': '4B'}]

def addItem():
    print('-------------------- 1.- Add Item ---------------------')
    itemName = input('Please type the name of the item: ')
    itemQuantity = int(input('Please type the item\'s quantity: '))
    itemPrice = float(input('Please type item\'s unit price: '))
    itemLocation = input('Please insert the item location: ')

    newItem = {'Name': itemName.lower(), 'Quantity': itemQuantity, 'Unit Price': itemPrice,
               'Location': itemLocation.upper()}
    print('This new item will be added:')
    print(newItem)
    inventory.append(newItem)


def updateItem():
    print('-------------------- 2.- Update Item ---------------------')
    while True:
        itemName = input('Please type the name of the item to be updated: ')
        itemToUpdate = []
        for i, item in enumerate(inventory):
            if item['Name'] == itemName.lower():
                itemToUpdate = item
                print('This is the item found:')
                print(itemToUpdate)
                while True:
                    print('Which field do you want to update?')
                    print('1.- Name')
                    print('2.- Quantity')
                    print('3.- Unit Price')
                    print('4.- Location')
                    option = int(input('Enter your option: '))
                    if option not in [1, 2, 3, 4]:
                        print('It is not a valid option, try again')
                        pass
                    valueToUpdate = input('Please type the new value: ')
                    fieldsToUpdate = ['Name', 'Quantity', 'Unit Price', 'Location']
                    fieldToUpdate = fieldsToUpdate[option - 1]
                    inventory[i][fieldToUpdate] = valueToUpdate
                    return
        if len(itemToUpdate) == 0:
            retry = input('The selected item does not exist, do you want to try again? (Y/N)')
            if retry.upper() == 'Y':
                pass
            elif retry.upper() == 'N':
                return


def searchItem():
    print('-------------------- 3.- Search Item ---------------------')
    while True:
        itemName = input('Please type the name of the item to search: ')
        itemToUpdate = list(filter(lambda item: item['Name'] == itemName.lower(), inventory))
        if (len(itemToUpdate) == 0):
            retry = input('The selected item does not exist, do you want to try again? (Y/N)')
            if retry.upper() == 'Y':
                pass
            elif retry.upper() == 'N':
                return
        else:
            print('This is the item found:')
            print(itemToUpdate[0])
            return


def sortInventory():
    print('-------------------- 4.- Sort Inventory ---------------------')
    while True:
        print('Which field do you want to use to sort the inventory?')
        print('1.- Name')
        print('2.- Quantity')
        print('3.- Unit Price')
        print('4.- Location')
        option = int(input('Enter your option: '))
        print(option)
        if option not in [1, 2, 3, 4]:
            print('It is not a valid option, try again')
            pass
        fields = ['Name', 'Quantity', 'Unit Price', 'Location']
        fieldToSortBy = fields[option - 1]
        inventory.sort(key=lambda item: item[fieldToSortBy])
        print('Here is the inventory sorted by ' + fieldToSortBy)
        for item in inventory:
            print(item)
        return

def generateReport():
    print('-------------------- 5.- Generate Report ---------------------')

    print('This is the current state of the inventory')
    for item in inventory:
        print(f"Name: {item['Name']} / Quantity: {item['Quantity']} / Unit Price: {item['Unit Price']} / Location: {item['Location']}")

def getTotalValue():
    print('-------------------- 6.- Total value ---------------------')
    print('The current total value of the inventory is:')
    totalValue = reduce(lambda a,b: a+b, map(lambda item: item['Quantity'] * item['Unit Price'], inventory))
    print("$" + str(totalValue))

def deleteItem():
    print('-------------------- 7.- Delete item ---------------------')
    while True:
        itemName = input('Please type the name of the item to be deleted: ')
        itemToDelete = []
        for i,item in enumerate(inventory):
            if item['Name'] == itemName.lower():
                itemToDelete = item
                print('This item will be deleted')
                print(itemToDelete)
                inventory.pop(i)
                return
        if len(itemToDelete) == 0:
            retry = input('The selected item does not exist, do you want to try again? (Y/N)')
            if retry.upper() == 'Y':
                pass
            elif retry.upper() == 'N':
                return

def inventoryManagerMenu():
    while True:
        print('------- Welcome to the Inventory Manager -------')
        print('-------------------- Menu ---------------------')
        print('-----------------------------------------------')
        print('Options:')
        print('1.- Add item')
        print('2.- Update item')
        print('3.- Search item')
        print('4.- Sort inventory')
        print('5.- Generate report')
        print('6.- Get total value of inventory')
        print('7.- Delete item')
        print('8.- Exit')
        print('-----------------------------------------------')

        option = int(input('Please select an option from the above: '))
        if (option == 1):
            addItem()
        if (option == 2):
            updateItem()
        if (option == 3):
            searchItem()
        if (option == 4):
            sortInventory()
        if (option == 5):
            generateReport()
        if (option == 6):
            getTotalValue()
        if (option == 7):
            deleteItem()
        if (option == 8):
            print('Thanks for using the Inventory Manager')
            break

inventoryManagerMenu()
