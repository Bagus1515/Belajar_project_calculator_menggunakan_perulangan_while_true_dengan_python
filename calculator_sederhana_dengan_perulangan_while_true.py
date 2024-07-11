# Logic
def penjumlahan(x, y):
    return x + y

def pengurangan(x, y):
    return x - y

def perkalian(x, y):
    return x * y

def pembagian(x, y):
    return x / y

# Untuk perulangan menggunakan while True
while True:
    print("\nCalculator Python")
    print("===================")
    print("1. PENJUMLAHAN")
    print("2. PENGURANGAN")
    print("3. PERKALIAN")
    print("4. PEMBAGIAN")
    print("5. EXIT")
    print("===================")

    # Untuk inputan menggunakan keyboard
    tipe = input("Silakan pilih: 1, 2, 3, 4, 5 (exit): ")
    
    if tipe in ("1", "2", "3", "4"):
        angka1 = float(input("Angka pertama: "))
        angka2 = float(input("Angka kedua: "))
        print("===================")

        # Menampilkan hasil berdasarkan pilihan tipe operasi
        if tipe == "1":
            print("Hasilnya adalah: ", penjumlahan(angka1, angka2))
        elif tipe == "2":
            print("Hasilnya adalah: ", pengurangan(angka1, angka2))
        elif tipe == "3":
            print("Hasilnya adalah: ", perkalian(angka1, angka2))
        elif tipe == "4":
            print("Hasilnya adalah: ", pembagian(angka1, angka2))

    elif tipe == "5":
        print("TERIMAKASIH (sampai jumpa)")
        break
    else:
        print("Pilihan tidak valid... silakan pilih nomor lagi")
