# Weight variable for shipping
try:
    weight = float(input("Enter the package weight: "))
    if weight <= 0:
        raise ValueError("Weight must be a positive number.")
except ValueError as e:
    print(f"Invalid input: {e}")
    weight = 0  # Default to 0 if invalid input is provided

# Ground shipping cost calculation
def calculate_ground_shipping(weight):
    if weight <= 2:
        return weight * 1.50 + 20
    elif weight <= 6:
        return weight * 3.00 + 20
    elif weight <= 10:
        return weight * 4.00 + 20
    else:
        return weight * 4.75 + 20

if weight > 0:
    ground_shipping_cost = calculate_ground_shipping(weight)
    print("Ground Shipping $", ground_shipping_cost)
else:
    ground_shipping_cost = float('inf')  # Set to infinity to exclude from comparison

# Ground shipping premium cost calculation
ground_premium_cost = 125.00
print("Ground Shipping Premium $", ground_premium_cost)

# Drone shipping cost calculation
def calculate_drone_shipping(weight):
    if weight <= 2:
        return weight * 4.50
    elif weight <= 6:
        return weight * 9.00
    elif weight <= 10:
        return weight * 12.00
    else:
        return weight * 14.25

if weight > 0:
    drone_shipping_cost = calculate_drone_shipping(weight)
    print("Drone Shipping $", drone_shipping_cost)
else:
    drone_shipping_cost = float('inf')  # Set to infinity to exclude from comparison

# Cheapest shipping method calculation
if weight > 0:
    if ground_shipping_cost < ground_premium_cost and ground_shipping_cost < drone_shipping_cost:
        print("Cheapest method: Ground Shipping $", ground_shipping_cost)
    elif ground_premium_cost < ground_shipping_cost and ground_premium_cost < drone_shipping_cost:
        print("Cheapest method: Ground Shipping Premium $", ground_premium_cost)
    else:
        print("Cheapest method: Drone Shipping $", drone_shipping_cost)
else:
    print("Unable to calculate shipping costs due to invalid weight.")