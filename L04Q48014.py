# Importing the random module
import random

# Defining a function 'test' that takes a 2D array 'a' as an input
def test(a):
    # Calculating the sum of values in each row of the array
    row1 = a[0][0] + a[0][1] + a[0][2]
    row2 = a[1][0] + a[1][1] + a[1][2]
    row3 = a[2][0] + a[2][1] + a[2][2]

    # Calculating the sum of values in each column of the array
    column1 = a[0][0] + a[1][0] + a[2][0]
    column2 = a[0][1] + a[1][1] + a[2][1]
    column3 = a[0][2] + a[1][2] + a[2][2]

    # Calculating the sum of values in each diagonal of the array
    diagnoal1 = a[0][0] + a[1][1] + a[2][2]
    diagnoal2 = a[1][2] + a[1][1] + a[2][1]

    # Checking if all sums are equal, i.e. if it's a Lo Shu Magic Square
    if(row1 == row2 == row3 == column1 == column2 == column3 == diagnoal1 == diagnoal2):
        print("It is a Lo Shu Magic Square")
    else:
        print("It is not a Lo Shu Magic Square")

# Initializing 3 arrays with 3 rows and 3 columns, filled with test cases
arr1 = [[4,9,2], [3,5,7], [8,1,6]]
arr2 = [[1,2,3], [4,5,6], [7,8,9]]
arr3 = [[6,1,2], [7,8,5], [3,4,1]]

# Calling the function three times for all test cases to check if its a Lo-Shu magic square
test(arr1)
test(arr2)
test(arr3)




