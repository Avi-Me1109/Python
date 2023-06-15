infile = open("numbers.txt", 'r')

a = len(infile.readlines())

infile.close()

i = 0
total = 0

# num_calc = open("numbers.txt", 'r')

# while(i < a):
#     num = int(num_calc.readline())

#     total = total + num

#     i = i+1

# num_calc.close()

num = open("numbers.txt", 'r')
for lines in num:
    number = int(num.readline())
    total = total + number

num.close()

print("The total is: ", total)