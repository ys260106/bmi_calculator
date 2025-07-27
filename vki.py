kg = float(input("Lütfen kilonuzu kilogram cinsinden giriniz = "))
boy = float(input("Lütfen boyunuzu metre cinsinden giriniz = "))

vki_degeri = kg / boy**2

if vki_degeri < 18.5:
    durum = "Zayıf"
elif vki_degeri < 25:
    durum = "Normal"
elif vki_degeri < 30:
    durum = "Fazla kilolu"
else:
    durum = "Obez"


print(f"Vücut Kitle İndeksiniz = {vki_degeri:.2f} ({durum})")
