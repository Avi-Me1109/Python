import random

lottery = []

for i in range(7):
    lottery.append(random.randint(0,9))

print("Lottery Number:")

for a in lottery:
    print(a, end="")