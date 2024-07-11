print("Calculator Python")
print("=================")

print("1. Penjumlahan")
print("2. Pengurangan")
print("3. Perkalian")
print("4. Pembagian")
print("=================")

#Logic
def penjumlahan(x,y):
    return x+y
def pengurangan(x,y):
    return x-y
def perkalian(x,y):
    return x*y
def pembagian(x,y):
    return x/y

tipe = input("Silakan Masukan Nomer yang kalian pilih : ")

if tipe in ("1", "2", "3", "4"):
    angka1 = float(input("angka pertama : "))
    angka2 = float(input("angka kedua : "))

    print("=================")
    if tipe == "1":
        print("jawabanya adalah : ",penjumlahan(angka1,angka2))
    if tipe == "2":
        print("jawabanya adalah : ", pengurangan(angka1,angka2))
    if tipe == "3":
        print("jawabanya adalah : ", perkalian(angka1,angka2))
    if tipe == "4":
        print("jawabanya adalah : ", pembagian(angka1,angka2))
    print("=================")