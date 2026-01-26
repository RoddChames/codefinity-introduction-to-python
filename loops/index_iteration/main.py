prices = [29.99, 45.50, 12.75, 38.20]
discounts = [0.9,0.8,0.85,0.95]
updated_price = 0.00


# Write your code here
for item in range(len(prices)):
    updated_price = (prices[item] * discounts[item])
    prices[item] = updated_price
    print(f"Updated price for item {item}: ${updated_price:.2f}")