#Lovely LoveSeat Receipt System

#Catalog Description
lovely_loveseat_description = "Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white."

stylish_settee_description = "Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black."

luxurious_lamp_description = "Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade."

#Catalog Prices
lovely_loveseat_price = 254.00

stylish_settee_price = 180.50

luxurious_lamp_price = 52.15

#Sales Tax
sales_tax = 0.088

#First Customer Variables 
customer_one_total = 0
customer_one_itemization = ""

#Calculate First Customer Total
customer_one_itemization = lovely_loveseat_description + "\n\n" + luxurious_lamp_description

def calculate_total(prices, tax):
    total = sum(prices)
    total_tax = total * tax
    return total + total_tax

customer_one_total = calculate_total([lovely_loveseat_price, luxurious_lamp_price], sales_tax)

#First Customer Receipt
print("Customer One Items:")
print(customer_one_itemization)
print()
print("Customer One Total:")
print(customer_one_total)
