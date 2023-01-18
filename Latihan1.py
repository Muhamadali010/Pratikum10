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