def largest(num, n):
    
    if n == 1:
        return(num[n-1])
       
    else:
        prev = largest(num, n-1)
        curr = num[n-1]
    
        if prev > curr:
            return prev
        else:
            return curr
    

print(largest([5,8,9], 3))