# List of product names
products = ["Banana", "Apple", "Mango", "Cherry"]

# List of product prices
prices = [1.20, 0.50, 2.50, 1.75]

# List of quantity sold
quantities_sold = [50, 100, 25, 40]

for products, prices, quantities_sold in zip(products,prices,quantities_sold):
    combined_list = products,prices,quantities_sold
    #sorted_products = sorted(combined_list)
    print(combined_list)
