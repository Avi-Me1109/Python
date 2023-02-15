denominator = 3
ans = 4

for i in range(0, 1000):
    ans = ans + 4/(denominator)
    denominator = denominator + 2
    
print(ans)