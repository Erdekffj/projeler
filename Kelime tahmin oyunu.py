import random

# Kelime listesi
kelimeler = ["elma", "armut", "çilek", "muz", "karpuz", "kiraz", "üzüm", "şeftali"]

# Rastgele bir kelime seçme
secilen_kelime = random.choice(kelimeler)

# Kullanıcıya kelimeyi tahmin etmesi için ipucu verme
print("Bir meyve ismi tahmin edin.")
print("Kelimenin uzunluğu: ", len(secilen_kelime))
print("İlk harfi: ", secilen_kelime[0])

# Kullanıcının tahmin etmesi
tahmin = input("Tahmininizi yazın: ")

# Doğru tahmin edene kadar ipucu verme ve tekrar tahmin alma
while tahmin != secilen_kelime:
    print("Yanlış tahmin. Tekrar deneyin.")
    tahmin = input("Tahmininizi yazın: ")

# Doğru tahmin edildiğinde tebrik etme
print("Tebrikler! Doğru tahmin ettiniz.")
