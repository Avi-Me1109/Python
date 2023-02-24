#Avi Raj Balam
#Lab 2 - Question 3
#2/24/2023
#A program that outputs the hashtag pattern in question 3

i = 0
a = 0
#incremental value for two while loops

while(i < 7):
    print("#", end = "")
    #printing first hashtag and same line
    while(a < i):
        print(" ", end = "")
        a = a + 1
    #printing amount of spaces determining on row number
    
    print("#")
    #printing second hashtag
    i = i + 1
    #increment
    a = 0
    #reinitialize inner while loop count
#main while loops to print the two hashtags