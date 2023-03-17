rainfall = []

for i in range(12):
    print("Month", (i+1))
    rainfall.append(int(input("Enter rainfall: ")))

sum = 0
greatest = -99999
smallest = 99999
for i in rainfall:
    sum = sum + i

    if(i > greatest):
        greatest = i

    if(i < smallest):
        smallest = i

average = sum / len(rainfall)

print("")

print("Total rainfall: ", sum)
print("Average rainfall: ", average)

print("Highest Month(s) in rainfall:")
for a in range(len(rainfall)):
    if(greatest == rainfall[a]):
        print(rainfall[a])


print("Lowest Month(s) in rainfall:")
for a in range(len(rainfall)):
    if(smallest == rainfall[a]):
        print(rainfall[a])