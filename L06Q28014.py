import random

#define dictionary of numbers
numbers = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0}

#for loop to generate 100 random numbers and count each time it is generated
for i in range (100):
    num = random.randint(1, 10)
    
    numbers[num] += 1

#print results
print(numbers)