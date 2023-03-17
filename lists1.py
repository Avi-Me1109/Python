numbers = [74, 19, 105, 20, -2, 67, 77, 124, -45, 38]
valid_numbers = []

for a in numbers:
    if(a >= 0 and a <= 100):
        valid_numbers.append(a)

sum = 0
for a in valid_numbers:
    sum = sum+a

average = sum / len(valid_numbers)
print("Total: ", sum)
print("Average: ", format(average, '.2f'))