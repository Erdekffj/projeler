import random

# Rastgele sayıyı seçin
number = random.randint(1, 100)

# Kullanıcıdan tahminler alın ve sayıyı doğru tahmin edene kadar devam edin
while True:
    guess = int(input("Tahmininiz nedir? "))
    if guess == number:
        print("Tebrikler, doğru tahmin ettiniz!")
        break
    elif guess < number:
        print("Daha yüksek bir sayı tahmin edin.")
    else:
        print("Daha düşük bir sayı tahmin edin.")
