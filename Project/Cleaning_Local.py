#Avi Raj Balam
#ADTP 2108014
#Local Airbnb Data Cleaning Python Script for correlation

#importing all libraries needed
import pandas as pd
import seaborn as sb
import numpy
import matplotlib.pyplot as plt
import re

#The Airbnb data is read from a CSV file using pandas and stored in the variable "Airbnb_Details".
Airbnb_Details = pd.read_csv("Project/MY_details.v2.csv")

#Obtaining all necessary data from the columns needed
Beds_num = Airbnb_Details['Sleeping_Arrangements'].tolist()
Location = Airbnb_Details['Location'].tolist()
Title = Airbnb_Details['Title'].tolist()
Page = Airbnb_Details['Page_URL'].tolist()
Price = Airbnb_Details['Price'].tolist()
Rating = Airbnb_Details['Rating'].tolist()
Num_Reviews = Airbnb_Details['Number_of_Reviews'].tolist()
Amenities = Airbnb_Details['Amenities'].tolist()

#extra lists for cleaned data
Beds = []
Avg_Bed = []
No_of_Amenities = []

#Data cleaning by removing rows with missing or incorrect values in certain columns such as "Sleeping_Arrangements", "Location", "Rating", "Price", and "Number_of_Reviews".
for i in range(len(Beds_num)-1, -1, -1):
    if(type(Beds_num[i]) == float):
        del(Beds_num[i])
        del(Location[i])
        del(Title[i])
        del(Page[i])
        del(Price[i])
        del(Rating[i])
        del(Num_Reviews[i])
        del(Amenities[i])

for i in range(len(Beds_num)-1, -1, -1):
    if(type(Location[i]) == float):
        del(Beds_num[i])
        del(Location[i])
        del(Title[i])
        del(Page[i])
        del(Price[i])
        del(Rating[i])
        del(Num_Reviews[i])
        del(Amenities[i])

for i in range(len(Rating)-1, -1, -1):
    if (pd.isna(Rating[i]) or pd.isna(Price[i]) or pd.isna(Num_Reviews[i])):
        del(Beds_num[i])
        del(Location[i])
        del(Title[i])
        del(Page[i])
        del(Price[i])
        del(Rating[i])
        del(Num_Reviews[i])
        del(Amenities[i])

#Removing rows that are not located in Penang by checking if the string "Pinang" is present in the "Location" column.
for i in range(len(Location)-1, -1, -1):
     if ("Pinang" not in Location[i]):
        del(Beds_num[i])
        del(Location[i])
        del(Title[i])
        del(Page[i])
        del(Price[i])
        del(Rating[i])
        del(Num_Reviews[i])
        del(Amenities[i])

#The script extracts the number of beds from the "Sleeping_Arrangements" column
for i in range(len(Beds_num)):
    if(type(Beds_num[i]) != float):
        Beds_num[i]= Beds_num[i].replace('Bedroom 1', '')
        Beds_num[i]= Beds_num[i].replace('Bedroom 2', '')
        Beds_num[i]= Beds_num[i].replace('Bedroom 3', '')
        Beds_num[i]= Beds_num[i].replace('Common space1', '')
        Beds_num[i]= Beds_num[i].replace('Common space2', '')
        Beds_num[i]= Beds_num[i].replace('Bedroom area', '')
        Beds_num[i]= Beds_num[i].replace('Living area1', '')
        Beds_num[i]= Beds_num[i].replace('Living area2', '')

#adding all beds together
for i in range(len(Beds_num)):
    numbers = re.findall('\d+', Beds_num[i])
    total = sum(int(num) for num in numbers)
    Beds.append(total)

# converts the price to an integer
for i in range(len(Price)):
     Price[i] = Price[i].replace('$', '')
     Price[i] = Price[i].replace('per night', '')
     Price[i] = Price[i].replace(' ', '')
     Price[i] = int(Price[i])

#calculates the number of amenities for each property
for i in range(len(Amenities)):
    values = Amenities[i].split('\n')
    num_values = len(values)
    No_of_Amenities.append(num_values)

#calculates the correlation coefficient between different variables and creates scatterplots for all question requirements.
corr = numpy.corrcoef(Beds, Price)
print("Correlation Beds vs Price:", + corr[0,1])
sb.scatterplot(x= Beds, y= Price)
plt.title('Beds vs Price')
plt.xlabel('Beds')
plt.ylabel('Price')
plt.show()
plt.close()

corr = numpy.corrcoef(Num_Reviews, Price)
print("Correlation Num_Reviews vs Price:", + corr[0,1])
sb.scatterplot(x= Num_Reviews, y= Price)
plt.title('Number of Reviews vs Price')
plt.xlabel('Number of Reviews')
plt.ylabel('Price')
plt.show()  
plt.close()

corr = numpy.corrcoef(Rating, Price)
print("Correlation Rating vs Price:", + corr[0,1])
sb.scatterplot(x= Rating, y= Price)
plt.title('Rating vs Price')
plt.xlabel('Rating')
plt.ylabel('Price')
plt.show()
plt.close()

corr = numpy.corrcoef(No_of_Amenities, Price)
print("Correlation Num_Amenities vs Price:", + corr[0,1])
sb.scatterplot(x= No_of_Amenities, y= Price)
plt.title('Number of Amenities vs Price')
plt.xlabel('Number of Amenities')
plt.ylabel('Price')
plt.show()
plt.close()

corr = numpy.corrcoef(Beds, Rating)
print("Correlation Beds vs Rating:", + corr[0,1])
sb.scatterplot(x= Beds, y= Rating)
plt.title('Beds vs Rating')
plt.xlabel('Beds')
plt.ylabel('Rating')
plt.show()
plt.close()

corr = numpy.corrcoef(Num_Reviews, Rating)
print("Correlation Num_Reviews vs Rating:", + corr[0,1])
sb.scatterplot(x= Num_Reviews, y= Rating)
plt.title('Number of Reviews vs Rating')
plt.xlabel('Number of Reviews')
plt.ylabel('Rating')
plt.show()
plt.close()

corr = numpy.corrcoef(Price, Rating)
print("Correlation Price vs Rating:", + corr[0,1])
sb.scatterplot(x= Price, y= Rating)
plt.title('Price vs Rating')
plt.xlabel('Price')
plt.ylabel('Rating')
plt.show()
plt.close()

corr = numpy.corrcoef(No_of_Amenities, Rating)
print("Correlation Amenities vs Rating:", + corr[0,1])
sb.scatterplot(x= No_of_Amenities, y= Rating)
plt.title('Number of Amenities vs Rating')
plt.xlabel('Number of Amenities')
plt.ylabel('Rating')
plt.show()
plt.close()

