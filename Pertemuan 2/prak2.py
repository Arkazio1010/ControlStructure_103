grade=int(input("masukkan grade: "))

if grade >= 90:
    print("Excellent performance")
elif grade >= 80:
    print("Very Good performance")
elif grade >= 70:
    print("Good performance")
elif grade >= 60:
    print("Average performance")
else:
    print("Poor performance")


angka1=int(input("masukkan angka pertama: "))
angka2=int(input("masukkan angka kedua: "))
angka3=int(input("masukkan angka ketiga: "))

if angka1 > angka2 and angka1 > angka3:
    print("angka pertama adalah yang terbesar")
elif angka2 > angka1 and angka2 > angka3:
    print("angka kedua adalah yang terbesar")
elif angka3 > angka1 and angka3 > angka2:
    print("angka ketiga adalah yang terbesar")
else:
    print("tidak ada angka yang terbesar")


n = int (input("Masukkan Jumlah Suku (n): "))
a, b = 0, 1

if n <=0:
    print("Masukkan angka positif")
elif n == 1:
    print("Deret Fibonacci: ", a)
else:
    print("Deret Fibonacci:", end=" ") 
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()


n = int(input("Masukkan Jumlah Suku (n): "))

print (f"Angka Ganjil Hingga {n} adalah:")
for i in range(1, n + 1, 2):
    print(i, end=" ")
print()