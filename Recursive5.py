def recursive_sum(numbers):
    if len(numbers) == 0:
        return 0
    else:
        return numbers[0] + recursive_sum(numbers[1:])

list = [1, 2, 3, 4, 5]
a = sum(list)
print(a)
