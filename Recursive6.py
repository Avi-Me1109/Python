def power(x, y):
    if y == 0:
        return 1
    else:
        return x * power(x, y-1)

a = power(2,3)
print(a)