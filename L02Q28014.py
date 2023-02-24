#Avi Raj Balam
#Lab 2 - Question 2
#2/24/2023
#A program that calculates sem fee for amount of years with a 3% increase every year

sem_fee = 8000
years = 5
#initalizing years and semester fee
i = 1
#initializing incrementer for while loop

while ( i < years):
    
    sem_fee = sem_fee * 1.03
    #increasing sem fee by 3% for every semester
    i = i + 1
    #increasing count
    
print("Projected Sem Tuition: ", format(sem_fee, ".2f"))
#outputting sem tuition