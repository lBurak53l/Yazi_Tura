import random

secenekler = ["yazı", "tura"]
skor = 0

print("--- YAZI - TURA OYUNU ---")
print("Çıkmak için 'q' yazın.\n")

while True:
    secim = input("Tahmininiz (yazı / tura): ").strip().lower()

    if secim == "q":
        print(f"\nOyun bitti! Toplam doğru tahmin: {skor}")
        break

    if secim not in secenekler:
        print("Geçersiz giriş. Yalnızca 'yazı' veya 'tura' yazın.\n")
        continue

    para = random.choice(secenekler)
    print(f"Para atıldı: {para.upper()} geldi!")

    if secim == para:
        skor += 1
        print(f"Tebrikler! Güncel Skor: {skor}\n")
    else:
        print(f"Bilemediniz. Güncel Skor: {skor}\n")