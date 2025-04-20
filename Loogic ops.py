# Operassi logika or
# Dibut untuk menentukan hasil dari A OR b

# Meminta imput dari penguna
# Imput berupa angka 0 (salah) satu 1 (benar)

a = int(input(masukan nilai A (0 untuk SALAH, 1 untuk BENAR):))
b = int(input("Masukan nilai B (0 untuk SALAH, 1 untuk BENAR):))

hasil = a or b

# Menamppilkan  hasilnya
print(f"Hasil dari(a)or(b)adalah:(hasil)")

a = 1
b = 0
# Hasil dari 1 OR 0 adalah: 1