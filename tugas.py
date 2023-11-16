# Inisialisasi list untuk menyimpan data mahasiswa
data_mahasiswa = []

# Fungsi untuk menghitung nilai akhir
def hitung_nilai_akhir(tugas, uts, uas):
    return round(0.3 * tugas + 0.35 * uts + 0.35 * uas, 1)

# Input data menggunakan perulangan
while True:
    print("\nMasukkan data mahasiswa:")
    nama = input("Nama        : ")
    nim = input("NIM         : ")
    nilai_tugas = int(input("Nilai Tugas : "))
    nilai_uts = int(input("Nilai UTS   : "))
    nilai_uas = int(input("Nilai UAS   : "))

    # Hitung nilai akhir
    nilai_akhir = hitung_nilai_akhir(nilai_tugas, nilai_uts, nilai_uas)

    # Tambahkan data ke dalam list
    data_mahasiswa.append({
        'Nama': nama,
        'NIM': nim,
        'Nilai Tugas': nilai_tugas,
        'Nilai UTS': nilai_uts,
        'Nilai UAS': nilai_uas,
        'Nilai Akhir': nilai_akhir
    })

    tambah_data = input("\nTambah Data(y/t)? ").lower()
    if tambah_data != 'y':
        break

# Tampilkan output dengan format tabel rata tengah
print("\n{:=^65}".format(""))
print("| No |    Nama      |      NIM     | Tugas | UTS | UAS | Akhir |")
print("{:=^65}".format(""))

for idx, mahasiswa in enumerate(data_mahasiswa, start=1):
    print("| {:<2} | {:^12} | {:^12} | {:^5} | {:^3} | {:^3} | {:^5} |".format(
        idx, mahasiswa['Nama'], mahasiswa['NIM'],
        mahasiswa['Nilai Tugas'], mahasiswa['Nilai UTS'],
        mahasiswa['Nilai UAS'], mahasiswa['Nilai Akhir']))
    print("{:-^65}".format(""))
