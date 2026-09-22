n = int(input("masukkan nilai n: "))

a = 0 
b = 1

for i in range(n + 1):
    if a > n:
        break
    print(a, end= " ")
    a, b = b, a + b


