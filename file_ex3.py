name = input("Enter the file name: ")

file = name + ".txt"

infile = open(file, 'r')

a = len(infile.readlines())

infile.close()

i = 1
qt = open(file, 'r')

while(i <= a):
    c = qt.readline()
    print(i, ":", c)
    i = i+1
    
qt.close()  

