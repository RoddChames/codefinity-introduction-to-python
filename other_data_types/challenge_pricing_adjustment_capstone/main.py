grocery_inventory = {
    "Milk":("Dairy",5.50,8),
    "Eggs":("Dairy",5.50,30),
    "Bread":("Bakery",2.99,15)
}

category, price, stock = grocery_inventory["Eggs"]
category, price, stock = grocery_inventory["Milk"]

if grocery_inventory["Eggs"][1] > 5:
    print("Eggs are too expensive, reducing the price by $1.")
    grocery_inventory["Eggs"] = (category,price -1,stock)
    #print(grocery_inventory["Eggs"])

grocery_inventory.update({"Tomatoes":("Produce",1.20,30)})
print("Inventory after adding Tomatoes: " + str(grocery_inventory))

if grocery_inventory["Milk"][2] < 10:
    print("Milk needs to be restocked. Increasing stock by 20 units.")
    grocery_inventory["Milk"] = (category, price, stock + 20)
    print("Updated inventory: " + str(grocery_inventory))
    