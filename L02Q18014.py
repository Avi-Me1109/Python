#Avi Raj Balam
#Lab 2 - Question 1
#2/24/2023
#A program that calculates total salary and salary per day by amount of days defined by user
#salary increases by 2 every day

salary = 1
#initialize salary
day = int(input("Enter number of days: "))
#get user input for days

print("Day    Salary")
#table headers

i = 1
#incremental count for while loop
sum = 0

while(i < (day+1)):
    
    print(i, end="       ")
    print("$", end = "")
    print(f"{(salary/100):,}")
    #printing day number and salary for each day
    sum = sum + salary
    #adding sum up from all salaries
    salary = salary * 2
    #exponentially increasing salary
    

    i = i+1
    #incrementing value


print("Total salary: $", end="")
print(f"{(sum/100):,}")
#printing final salary
