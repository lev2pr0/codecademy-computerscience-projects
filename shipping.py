#Weight variable for shipping 
weight = 41.5

#Ground shipping cost calculation

def calculate_ground_shipping(weight):
    if weight <= 2:
        return weight * 1.50 + 20
    elif weight <= 6:
        return weight * 3.00 + 20
    elif weight <= 10:
        return weight * 4.00 + 20
    else:
        return weight * 4.75 + 20

ground_shipping_cost = calculate_ground_shipping(weight)

print("Ground Shipping $", ground_shipping_cost)

#Ground shipping premium cost calculation
ground_premium_cost = 125.00

print("Ground Shipping Premium $", ground_premium_cost)


#Drone shipping cost calculation
def calculate_drone_shipping(weight):
    if weight <= 2:
        return weight * 4.50
    elif weight <= 6:
        return weight * 9.00
    elif weight <= 10:
        return weight * 12.00
    else:
        return weight * 14.25
drone_shipping_cost = calculate_drone_shipping(weight)
print("Drone Shipping $", drone_shipping_cost)

#Cheapest shipping method calculation
if ground_shipping_cost < ground_premium_cost and ground_shipping_cost < drone_shipping_cost:
    print("Cheapest method: Ground Shipping $", ground_shipping_cost)
elif ground_premium_cost < ground_shipping_cost and ground_premium_cost < drone_shipping_cost:
    print("Cheapest method: Ground Shipping Premium $", ground_premium_cost)
else:
    print("Cheapest method: Drone Shipping $", drone_shipping_cost)