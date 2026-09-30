isim1 = input("1. ürün adı: ")
fiyat1 = float(input("1. ürün fiyatı: "))
adet1 = int(input("1. ürün adedi: "))

isim2 = input("2. ürün adı: ")
fiyat2 = float(input("2. ürün fiyatı: "))
adet2 = int(input("2. ürün adedi: "))

toplam1 = fiyat1 * adet1
toplam2 = fiyat2 * adet2

print("\n--- SEPET ---")
print(isim1, ":", toplam1, "TL")
print(isim2, ":", toplam2, "TL")

print("Toplam:", toplam1 + toplam2, "TL")
