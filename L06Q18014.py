# Define a dictionary with the gifts for each day
gifts = {
    1: "a Partridge in a Pear Tree",
    2: "two Turtle Doves",
    3: "three French Hens",
    4: "four Calling Birds",
    5: "five Gold Rings",
    6: "six Geese-a-Laying",
    7: "seven Swans-a-Swimming",
    8: "eight Maids-a-Milking",
    9: "nine Ladies Dancing",
    10: "ten Lords-a-Leaping",
    11: "eleven Pipers Piping",
    12: "twelve Drummers Drumming"
}

# Define a list of the days in the song
days = [
    "first", "second", "third", "fourth", "fifth", "sixth",
    "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth"
]

# Use a for loop to generate the lyrics of the song
for i in range(12):
    # Print the day of the song
    print(f"On the {days[i]} day of Christmas, my true love gave to me:")
    
    # Print the gifts for that day and all the previous days
    for j in range(i, -1, -1):
        if j == 0 and i != 0:
            print("and", end=" ")
        print(gifts[j+1], end="")
        if j != 0:
            print(",", end=" ")
        print("\n")