grocery_inventory = {
    "Milk":("Dairy",5.50,8),
    "Eggs":("Dairy",5.50,30),
    "Bread":("Bakery",2.99,15)
}


egg_price = grocery_inventory["Eggs"][1]
print(egg_price)
#print(grocery_inventory["Eggs"][1])

if grocery_inventory["Eggs"][1] > 5:
    print("Eggs are too expensive, reducing the price by $1 ")
    grocery_inventory.update({"Eggs":("Dairy",4.50,30)})
    print(grocery_inventory["Eggs"][1])
    