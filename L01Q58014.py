#Avi Raj Balam
#Lab 1 - Question 5
#13/02/2023
#A program that makes the calculation for the vineyard owner on how many vines in a row

#Declaration of variables whose values are based on user inputs
R = float(input("Enter length of row (feet): "))

if (R < 0 ):
    
    print("Please retry and input appropriate values")
    
    
E = float(input("Enter amount of space used by end-post assembly (feet): "))

if (E < 0 ):
    
    print("Please retry and input appropriate values")
    
S = float(input("Enter space between vines (feet): "))

if (S < 0 ):
    
    print("Please retry and input appropriate values")
    

#Formula from question which makes use of previous user-input variables 

V = (R - (2*E)) / S

#Output to inform user of solution to formula with user defined inputs

if(V >= 0):
    print("Number of grapevines that can fit in row: ",int(V))

else:
    print("Given dimensions not valid")