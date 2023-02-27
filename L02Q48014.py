#Avi Raj Balam
#Lab 2 - Question 4
#2/24/2023
#A program to find the largest number within the given user inputs

count = 6
#counts amount of numbers can enter
largest = float("-inf")
# declaration of required variables of counter and largest number
# largest number set to negative infinity

i = 0
#counter

while(i < count):
    number = float(input("Enter a number: "))

    if (number == ""):
        print("Incorrect Input")
        print("Program Terminated")
        break

    #Getting user input
    if(largest < number):
        largest = number
    #condition to replace largest variable with number
    
    i = i+1
    #incrementer

#while loop to find largest number

print("The largest number you have entered is: ", largest)
#outputting value