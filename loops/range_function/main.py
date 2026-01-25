# List of products on promotion for each weekday
daily_promotions = ["Milk", "Eggs", "Bread", "Apples", "Oranges"]

# List of weekdays corresponding to the promotions
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

# Write your code here
for product in range(5):
    print(f"{weekdays[product]}: Promotion on {daily_promotions[product]}")
    