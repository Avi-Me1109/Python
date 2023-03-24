import random

def roll(throws):
    
    lt = []
    
    for i in range(throws):
        lt.append(random.randint(1,6))
        lt.sort

    return lt

no_of_throws = int(input("Enter the number of throws: "))
sorted_listed = roll(no_of_throws)

print(sorted_listed)