def calculate_discount(price, discount_percent):
    if discount_percent >=20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price
    
original_price = float(input("Enter the original price of an item: "))
discount_percentage = float(input("Enter the discount percentage of an item: "))
                               
final_price = calculate_discount(original_price, discount_percentage)

if final_price != original_price:
    print("The price is ", final_price, " Discount was applied")
else:
    print("The price is ", original_price, " No discount was applied")