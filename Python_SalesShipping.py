# Sal's Shipping
# 1
def ground_shipping(weight):
  ground_cost = ""
  if weight <= 2:
    ground_cost = weight * 1.5 + 20.0
  elif weight <= 6:
    ground_cost = weight * 3.0 + 20.0
  elif weight <= 10:
    ground_cost = weight * 4.0 + 20.0
  else:
    ground_cost = weight * 4.75 + 20.0
  return ground_cost

# 2
print(ground_shipping(8.4))

# 3
premium_ground_shipping = 125.0 

# 4
def drone_shipping(weight):
  drone_cost = ""
  if weight <= 2:
    drone_cost = weight * 4.5
  elif weight <= 6:
    drone_cost = weight * 9.0
  elif weight <= 10:
    drone_cost = weight * 12.0
  else:
    drone_cost = weight * 14.25

  return drone_cost

# 5
print(drone_shipping(1.5))

# 6
ground_price = ""
drone_price = ""

def cost_calculator(weight):

  ground_price = ground_shipping(weight)
  drone_price = drone_shipping(weight)
  final_price = ""
  method = ""

  if ground_price < drone_price and ground_price <  premium_ground_shipping:
    final_price = ground_price
    method = "Ground Shipping"

  elif drone_price < ground_price and drone_price <  premium_ground_shipping:
    final_price = drone_price
    method = "Drone Shipping"
  
  else:
    final_price = premium_ground_shipping
    method = "Premium Ground Shipping"

  return "The cheapest way to ship " + str(weight) + " pound package is using " + method + " and it will cost $" + str(final_price) + ".\n"

print(cost_calculator(4.8))
print(cost_calculator(41.5))