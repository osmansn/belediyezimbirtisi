with open('tss.txt', 'r') as dosya:
    satirlar = dosya.readlines()

# Satırları bir diziye kaydetmek
satir_dizisi = [satir.strip() for satir in satirlar]

# Sonuçları görüntüleme
print(satir_dizisi[2])

for strr in satir_dizisi:
    if strr in "mahalle adı fian":
        print("no biç")
    else:
        print("yes biç")


from datetime import datetime

# Şu anki tarihi al
bugun = datetime.today()

# Tarihi istediğimiz formatta biçimlendir
tarih_str = bugun.strftime("%Y-%m-%d")
budabistr="siksddsds'burayayaz'"
print(tarih_str)
budabistr=budabistr.replace("burayayaz",tarih_str)
print(budabistr)

