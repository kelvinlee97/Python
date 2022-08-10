def trip_planner_welcome(name):
  print("Welcome to tripplanner v1.0 " + str(name))

trip_planner_welcome("Singapore")

def estimated_time_rounded(estimated_time):
  rounded_time = round(estimated_time)
  return rounded_time
  
estimate = estimated_time_rounded(4.43)

def destination_setup(origin, destination, estimated_time, mode_of_transport = "Car"):
  print("Your trip starts off in " + str(origin))
  print("And you are traveling to " + str(destination))
  print("You will be traveling by " + str(mode_of_transport))
  print("It will take approximately " + str(estimated_time) + " hours")

destination_setup("Malaysia", "Singapore", estimate)