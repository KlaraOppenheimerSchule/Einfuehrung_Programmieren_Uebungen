def Fibbonacci(n,temp):
    print(n)
    # Beispiel: 2 = 1 + 2
    n = temp + n
    # Beispiel: 1 = 2 - 1
    temp = n - temp  
    if n < 1000:
        Fibbonacci(n,temp)
    else :
        print("Ende")
        pass

temp = 0
n = 1
Fibbonacci(n,temp)