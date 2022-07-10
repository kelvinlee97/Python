weight = float(input("How much the weight of ground shipping is: "))
weight_drone = float(input("How much the weight of drone shipping is: "))
cost_ground = float()
cost_ground_premium = 125.00
cost_drone = float()

########################
### Ground_Shippping ###
########################
## Weight of Ground_Shippping
########################
if weight <= 2:
  cost_ground = 1.5 * weight + 20
elif weight > 2 and weight <= 6:
  cost_ground = 3 * weight + 20
elif weight > 6 and weight <= 10:
  cost_ground = 4 * weight + 20
elif weight > 10:
  cost_ground = 4.75 * weight + 20
else:
  print("Not Found")


########################
### Total cost of Ground_Shippping ###
########################
print("The total cost_ground will be: ", + cost_ground)


########################
### Ground_Shippping_Premium ###
########################

### that is NO weight limit for Ground_Shippping_Premium ###

########################
### Total cost of Ground_Shippping_Premium ###
########################
print("The total cost_ground_premium will be: ", + cost_ground_premium)


########################
### Drone_Shipping ###
########################
## Weight of Drone_Shipping
########################
if weight_drone <= 2: 
  cost_drone = 4.5 * weight_drone
elif weight_drone > 2 and weight_drone <= 6: 
  cost_drone = 9 * weight_drone
elif weight_drone > 6 and weight_drone <= 10: 
  cost_drone = 12 * weight_drone
elif weight_drone > 10: 
  cost_drone = 14.25 * weight_drone
else:
  print("Not Found")

########################
### Total cost of Drone_Shipping ###
########################
print("The total cost_drone will be: ", + cost_drone)
