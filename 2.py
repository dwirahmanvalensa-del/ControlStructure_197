a = float(input("masukkan bilangan pertama: "))
b = float(input("masukkan bilangan kedua: "))
c = float(input("masukkan bilangan ketiga: "))

if a > b and a > c:
    largest = a
    print("angka terbesar adalah:",largest)
elif b > a and b > c:
    largest = b
    print("angka terbesar adalah:",largest)
elif c > a and c > b:
    largest = c
    print("angka terbesar adalah:",largest)
else:
    print("tidak angka terbesar")