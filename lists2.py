key = int(input("Enter the key number needed to find: "))

list_of_items = [10, 20, 30, 40, 50]
check = False

for a in list_of_items:
    if(a == key):
        check = True
        break

    else:
        check = False

if(check == True):
    print("Linear Search Success")
    print(key, "exists")

else:
    print("Linear Search Unsuccessful")
    print(key, "does not exist")



    
        