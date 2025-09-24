import sys
nilai =""

masuk =int(input("masukkan nilai ?"))
if masuk > 90:
    nilai("Nilai A")
elif masuk > 80 :
    nilai("Nilai B")
elif masuk > 70:
    nilai("Nilai C")
else :
    nilai("Nilai D")

lanjut =input("apakah lanjut ?")
if lanjut == 't':
    print('selesai')