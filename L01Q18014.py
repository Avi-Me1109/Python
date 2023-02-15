length = 12
width = 7
depth = 2
flow = 17
# declaring all necessary variables as stated in lab instructions: length, depth and width of pool, and flow of pipe

volume = length * width * depth
#calculating the volume of the pool
time = volume/flow
# rearranging formula to calculate time taken

print("The time taken would be: ", format(time, '.2f'), "hours")
# outputting the time taken in hours and in two decimal place for better user experience