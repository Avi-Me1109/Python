def multiply(x, y):
    if y == 0:
        return 0
    else:
        return x + multiply(x, y-1)
        
a = multiply(7, 4)
print(a)    