denominator = 3
ans = 4

for i in range(0, 199999):
    if(i % 2 == 0):
        ans = (ans - 4/(denominator))
        
    
    else:
        ans = (ans + 4/(denominator))
        
    
    denominator = denominator + 2
    # print(ans)

print(format(ans, '.5f'))