def potenz20 (n):
    if(n==1):
        return 20
    else:
        return 20 * potenz20(n-1)
    
for i in range(1,10):
    print(potenz20(i))
