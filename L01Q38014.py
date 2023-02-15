speed_limit = int(input("Enter the speed limit of area: "))
# getting input of speed limit of the area
clocked_speed = float(input("Enter the clocked speed of vehicle: "))
# getting clocked speed of a vehicle
fine = 0
# declaring a variable of fine

if(clocked_speed <= speed_limit):
    print("Driving within legal speed limit")
    # if the clocked speed is less than speed limit, printing legal speed limit

if(clocked_speed > speed_limit):
    excess = clocked_speed - speed_limit
    fine = 50 + (excess * 5)
    # if clocked speed more than speed limit, getting extra speed above speed limit
    # adding base $50 and ($5 * excess speed)

    if(clocked_speed > (90 + speed_limit)):
        fine = fine + 200
        # extra fine if the clocked speed is 90mph more than speed limit

    print("You have exceed the speed limit!")
    print("Your speed was: ", clocked_speed)
    print("Fine: ", fine)
    # outputting message, clocked speed and fine