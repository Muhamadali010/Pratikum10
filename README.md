# Pratikum10

Nama    :   Muhamad Ali M</br>
NIM     :   312210540</br>
Kelas   :   TI.22.B2</br>

# Pertemuan 14 : Python String
### Apa itu Python String?
- String adalah jenis yang paling populer di Python.
- Untuk membuatnya hanya dengan melampirkan karakter dalam tanda kutip.
- Python memperlakukan tanda kutip tunggal sama dengan tanda kutip ganda.
- Membuat string semudah memberi nilai pada sebuah variabel.
### 1. Latihan1

```py
txt = 'Hello World'
print()

# Hitung jumlah karakternya
print("====================================================")
print("| Jumlah karakter                   : ",len(txt),"\t\t   |")
print("====================================================")

# Ambil karakter terakhir
print("| Karakter terakhir                 : ",txt[-1],"\t\t   |")
print("====================================================")

# Ambil karakter index ke-2 sampai index ke-4 (llo)
print("| Karakter indek ke-2 sampai ke-4   : ",txt[2:5],"\t\t   |")
print("====================================================")

# Hilangkan spasi pada text tersebut (HelloWord)
print("| Menghilangkan spasi               : ",txt.replace(" ","")," |")
print("====================================================")

# Ubah text menjadi huruf besar
print("| Mengubah text menjadi huruf besar : ",txt.upper(),"|")
print("====================================================")

# Ubah text menjadi huruf kecil
print("| Mengubah text menjadi huruf kecil : ",txt.lower(),"|")
print("====================================================")

# Ganti karakter H dengan karakter J
print("| Mengganti karakter H dengan J     : ",txt.replace("H","J"),"|")
print("====================================================")
```

### 2. Latihan2
```py
umur = 24
txt = "\nHello, nama saya John, dan umur saya adalah {0} tahun\n"
```
print(txt.format(umur))
### Source Code
![img2](SS/SS3.PNG)
![img2](SS/SS4.PNG)
### A. Penjelasan Latihan 1
1.  Untuk menghitung karakter pada string yaitu menggunakan Fungsi `len()`.</br>
Contoh:
```py
print(len(txt))
```
Fungsi len() pada python di gunakan untuk menghitung karakter pada string.
- Fungsi len() pada python di gunakan untuk menghitung karakter pada string.

2. Jika ingin mengambil karakter terakhir, gunakan index `[-1]`.</br>
Contoh:
@@ -72,7 +72,7 @@ print(txt.replace("H", "J"))

### B. Penjelasan Latihan 2

Untuk memasukkan variable ke dalam string, tambahkan kurung kurung awal dan kurung akhir `{}` untuk menempatkan variable sebelumnya.</br>
- Untuk memasukkan variable ke dalam string, tambahkan kurung kurung awal dan kurung akhir `{}` untuk menempatkan variable sebelumnya.</br>
Contoh:
```py
    umur = 24
    
    txt = "Hello, nama saya john, dan umur saya adalah {0} tahun"
    print(txt.format(umur))
```
### C. Hasil Output
- Latihan 1</br>
![img2](SS/SS5.PNG)
- Latihan 2</br>
![img2](SS/SS6.PNG)
# *SEKIAN, TERIMA KASIH :)*
