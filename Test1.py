infile = open("sales.txt", 'r')

a = len(infile.readlines())
i = 1

infile.close()

infile = open("sales.txt", 'r')

value = 0

while(i <= a):
    if(i % 2 == 0):
        value = abs(int(infile.readline()))
        a = 0
        while(a < value):
            print("*", end = "")
            a = a+10000
        print()
    
    else:
        month = infile.readline()
        print(month, "-22:", end = "")

    i = i+1

infile.close()