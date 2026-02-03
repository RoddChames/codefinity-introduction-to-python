# Grocery store inventory:
# "Item": [current stock, target stock level, restock amount]
inventory = {
    "Bread": [30, 50, 10],
    "Eggs": [120, 200, 40],
    "Milk": [60, 100, 20],
    "Apples": [15, 50, 15]
}

print("Restocking started")


# Write your code here


for item in inventory:
    print(f"Restocking {item}")
    current_stock, target_stock_level, restock_amount = inventory[item]
    #print(inventory[item])
    while current_stock < target_stock_level:
        current_stock += restock_amount
        print(current_stock)
        inventory[item][0] = current_stock


print("Restocking completed")