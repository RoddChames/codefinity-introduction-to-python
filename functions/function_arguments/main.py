def apply_discount(price, discount=0.10):
    discount = price * discount
    price_after_discount = price - discount
    return price_after_discount

def add_tax(price, tax=0.05):
    tax = price * tax
    after_tax_added = price + tax
    return after_tax_added

def final_price(price, discount=0.10, tax=0.05):
    x = apply_discount(price, discount)  
    y = add_tax(x, tax)
    return y 
 

final_price_default = final_price(50)
final_price_custom = final_price(50, tax=0.08)


print(f"Final price with default discount and tax: ${final_price_default}")
print(f"Final price with custom tax: ${final_price_custom}")

