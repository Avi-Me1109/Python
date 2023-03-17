import random # import the random module

def flip(): # define a function called flip
    return random.randint(0, 1) # return a random integer between 0 and 1 (inclusive)

heads_count = 0 # initialize heads_count variable to 0
tails_count = 0 # initialize tails_count variable to 0

for i in range(0,100): # iterate over the range of numbers from 0 to 99 (inclusive)
    result = flip() # call the flip function and store its return value in result variable
    if result == 0: # if result is equal to 0
        tails_count += 1 # increment tails_count by 1
        #print("Tails")
    else: 
        heads_count += 1 # increment heads_count by 1
        #print("Heads")

print("Heads count:", heads_count) # print out the final count of heads
print("Tails count:", tails_count) # print out the final count of tails