# Buat list sebanyak 5 elemen dengan nilai bebas
my_list = [10, 20, 30, 40, 50]

# Akses list
# Tampilkan elemen ke 3
print("Elemen ke-3:", my_list[2])

# Ambil nilai elemen ke 2 sampai elemen ke 4
print("Elemen ke-2 sampai ke-4:", my_list[1:4])

# Ambil elemen terakhir
print("Elemen terakhir:", my_list[-1])

# Ubah elemen list
# Ubah elemen ke 4 dengan nilai lainnya
my_list[3] = 45

# Ubah elemen ke 4 sampai dengan elemen terakhir
my_list[3:] = [45, 55, 65]

# Tambah elemen list
# Ambil 2 bagian dari list pertama (A) dan jadikan list ke 2 (B)
list_A = my_list[:2]
list_B = my_list[2:]

# Tambah list B dengan nilai string
list_B.append("hello")

# Tambah list B dengan 3 nilai
list_B.extend([1, 2, 3])

# Gabungkan list B dengan list A
new_list = list_A + list_B

# Tampilkan hasil akhir
print("List setelah modifikasi:", new_list)
