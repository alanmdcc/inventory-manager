# Inventory Manager
--------------------------------

This is the menu where you can choose what action to take
```
------- Welcome to the Inventory Manager -------
-------------------- Menu ---------------------
-----------------------------------------------
Options:
1.- Add item
2.- Update item
3.- Search item
4.- Sort inventory
5.- Generate report
6.- Get total value of inventory
7.- Delete item
8.- Exit
-----------------------------------------------
```

### 1.- Add Item
You can add a new item. 
You have to type the following fields:
* Name of the item
* Quantity of pieces (integer)
* Unit price in dollars (two decimal places)
* Location in the storage

### 2.- Update Item
You can update the data of an item.
* First you have to type the name of the product you want to update (not case-sensitive). If no product is found, you will be asked if you want to try again.
* Then you will have to pick which field to update, either Name/Quantity/Unit Price/Location
* Afterward you'll be asked to provide the new value
* Finally, you'll see printed the updated record

### 3.- Search item
You can search and show the data of an item.
* You have to type the name of the product you want to visualize (not case-sensitive). If no product is found, you will be asked if you want to try again.
* Tha info of the item found will be displayed

### 4.- Sort inventory
Sort the current inventory based on the column that is chosen.
* Select which field to use to sort, either Name/Quantity/Unit Price/Location
* The inventory will be displayed already sorted in ascending way based on the chosen field

### 5.- Generate report
A report will be generated with the current inventory info
```
This is the current state of the inventory
Name: apple / Quantity: 20 / Unit Price: 3.50 / Location: 4B
Name: car / Quantity: 12 / Unit Price: 20000.00 / Location: 3B
Name: laptop / Quantity: 40 / Unit Price: 10000.00 / Location: 5F
```

### 6.- Get total value of inventory
The total value will be displayed, which is sum of unit price times the quantity for each item in inventory

### 7.- Delete item
* You have to type the name of the product you want to delete (not case-sensitive). If no product is found, you will be asked if you want to try again.
* Tha info of the item found and that was deleted will be displayed

### 8.- Exit
Exit the application


