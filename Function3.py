def prime (num):
    prime_num = True
    
    for i in range (2,num):
        if(num % i) == 0:
            prime_num = False
            break

    return prime_num

number = int(input("Enter a number: "))
determiner = prime(number)

if(determiner == True):
    print("The number is a prime.")

else:
    print("The number is not a prime.")