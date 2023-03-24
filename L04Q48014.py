import random

def test(a):
    row1 = a[0][0] + a[0][1] + a[0][2]
    row2 = a[1][0] + a[1][1] + a[1][2]
    row3 = a[2][0] + a[2][1] + a[2][2]

    column1 = a[0][0] + a[1][0] + a[2][0]
    column2 = a[0][1] + a[1][1] + a[2][1]
    column3 = a[0][2] + a[1][2] + a[2][2]

    diagnoal1 = a[0][0] + a[1][1] + a[2][2]
    diagnoal2 = a[1][2] + a[1][1] + a[2][1]

    if(row1 == row2 == row3 == column1 == column2 == column3 == diagnoal1 == diagnoal2):
        print("It is a Lo Shu Magic Square")
    
    else:
        print("It is not a Lo Shu Magic Square")

rows, cols = (3,3)
arr1 = [[0]*cols]*rows
arr2 = [[0]*cols]*rows
arr3 = [[0]*cols]*rows

for i in range(3):
    for a in range(3):
        arr1[i][a] = random.randint(1,9)
        arr2[i][a] = random.randint(1,9)
        arr3[i][a] = random.randint(1,9)

test(arr1)
test(arr2)
test(arr3)




