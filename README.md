# Praktikum 5

## Latihan 1

1. Pembuatan List: List dalam Python adalah kumpulan elemen dengan nilai bebas. Contohnya<br>
   `my_list = [10, 20, 30, 40, 50]`

2. Akses Elemen List:

- Elemen ke-3 dapat diakses dengan menggunakan indeks 2, contohnya, `my_list[2]`
- Mengambil nilai elemen ke-2 sampai ke-4 dengan slicing, misalnya, `my_list[1:4]`
- Elemen terakhir dapat diambil dengan indeks -1, yaitu, `my_list[-1]`

3. Perubahan Elemen List:

- Mengubah nilai elemen ke-4 dengan nilai lain, seperti, `my_list[3] = 45`
- Mengubah elemen ke-4 sampai dengan elemen terakhir, contohnya, `my_list[3:] = [45, 55, 65]`

4. Penambahan Elemen List:

- Membuat dua bagian dari list pertama dan membentuk list kedua, seperti, `list_A = my_list[:2]` dan `list_B = my_list[2:]`
- Menambahkan nilai string ke list B dengan `list_B.append("hello")`
- Menambahkan 3 nilai ke list B dengan `list_B.extend([1, 2, 3])`

5. Gabungan List:

- Menggabungkan list B dengan list A menjadi list baru, yaitu, `new_list = list_A + list_B`

6. Hasil Akhir:

- Menampilkan list setelah modifikasi dengan `print("List setelah modifikasi:", new_list)
![Screenshot_20231116_201253](https://github.com/ficzclay/praktikum5/assets/148204078/5f11507d-0fca-43bf-9976-d1a5f505f54a)



## Tugas Praktikum

Buat program sederhana untuk menambahkan data kedalam sebuah
list dengan rincian sebagai berikut:

- Progam meminta memasukkan data sebanyak-banyaknya (gunakan
  perulangan)
- Tampilkan pertanyaan untuk menambah data (y/t?), apabila jawaban
  t (Tidak), maka program akan menampilkan daftar datanya.
- Nilai Akhir diambil dari perhitungan 3 komponen nilai (tugas: 30%,
  uts: 35%, uas: 35%)
- Buat flowchart dan penjelasan programnya pada README.md.
- Commit dan push repository ke github.

Program ini digunakan untuk menginput nilai mahasiswa dan menghitung nilai akhir berdasarkan bobot tugas, UTS, dan UAS.

1. Inisialisasi List: Program dimulai dengan membuat list kosong data_mahasiswa untuk menyimpan data mahasiswa.

2. Fungsi Hitung Nilai Akhir: Terdapat fungsi `hitung_nilai_akhir(tugas, uts, uas)` yang menghitung nilai akhir dengan bobot tertentu untuk tugas, UTS, dan UAS.

3. Input Data Mahasiswa: Program menggunakan perulangan while True untuk terus meminta input data mahasiswa. Pengguna diminta untuk memasukkan nama, NIM, nilai tugas, UTS, dan UAS.

4. Perhitungan Nilai Akhir: Program menghitung nilai akhir menggunakan fungsi hitung_nilai_akhir dan menyimpan seluruh data dalam bentuk dictionary yang ditambahkan ke dalam list data_mahasiswa.

5. Tampilan Output: Hasil akhir ditampilkan dalam format tabel dengan rata tengah. Setiap baris menampilkan nomor, nama, NIM, nilai tugas, UTS, UAS, dan nilai akhir untuk setiap mahasiswa.

6. Perulangan Input Data: Setelah satu data dimasukkan, program menanyakan apakah ingin menambahkan data mahasiswa lagi. Perulangan berlanjut sampai pengguna tidak ingin menambahkan data lagi.

Berikut Hasilnya:

![Screenshot_20231116_202815](https://github.com/ficzclay/praktikum5/assets/148204078/6f9e9cd6-a9e3-4e4e-ac94-1c34a12152fe)


Flowchart:<br>
<img width="338" alt="3" src="https://github.com/ficzclay/praktikum5/assets/148204078/2aa82fde-29a6-42a7-9f64-a97bd41b7a0c">


## Langkah-langkah pengerjaan latihan

1. Konfigurasi terlebih dahulu username dan email pada global repository-nya

```
git config --global user.name “nama_user”
```

```
git config --global user.email “email_user”
```

2. Buat repository local

```
mkdir bahasa_pemrograman
```

```
cd bahasa_pemrograman
```

```
mkdir praktikum5
```

3. Jika sudah, jalankan command (command git init digunakan untuk menginisialisasi repositori git baru)

```
git init
```

## Menambahkan File Baru Pada Repository Lokal

1. Untuk membuat file baru bisa juga dengan text editor

disini akan menggunakan terminal

```
echo “# praktikum5 >> README.md
```

2. Untuk menambahkan file yang baru saja dibuat, gunakan command

```
git add README.md
```

3. Untuk menyimpan perubahan yang ada pada database repositori
   lokal, gunakan command

```
git commit -m "first commit"
```

## Membuat Repository Server

1. Server repository yang digunakan adalah github
2. Buat akun github terlebih dahulu
3. Klik tombol + new repository
4. Isi nama repository-nya,

```
contoh: praktikum5
```

5. lalu klik tombol Create repository

## Menambahkan Remote Repository

- Remote Repository merupakan server repositori yang akan digunakan untuk menyimpan segala perubahan yang dilakukan pada repositori lokal, dan bisa diakses oleh banyak pengguna
- Untuk menambahkan remote repository server, gunakan command

```
git remote add origin [url]
```

## Mengirim perubahan ke server (Push)

- Untuk mengirim perubahan pada repositori lokal ke server, gunakan command

```
git push -u origin master
```

## Clone Repository

- git clone digunakan untuk mengambil salinan dari repositori Git dari server ke repositori lokal
- gunakan command ini untuk melakukan kloning ke repositori lokal

```
git clone [url]
```
