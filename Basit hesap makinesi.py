while True:
    print("Yapmak istediğiniz işlemi seçin:")
    print("1. Toplama")
    print("2. Çıkarma")
    print("3. Çarpma")
    print("4. Bölme")
    print("0. Çıkış")
    
    choice = int(input("Seçiminiz (0/1/2/3/4): "))
    
    if choice == 0:
        print("Hesap makinesi kapatılıyor.")
        break
    
    num1 = float(input("Birinci sayıyı girin: "))
    num2 = float(input("İkinci sayıyı girin: "))
    
    if choice == 1:
        result = num1 + num2
        print("Toplam: ", result)
    elif choice == 2:
        result = num1 - num2
        print("Fark: ", result)
    elif choice == 3:
        result = num1 * num2
        print("Çarpım: ", result)
    elif choice == 4:
        if num2 == 0:
            print("Bir sayıyı sıfıra bölemezsiniz!")
        else:
            result = num1 / num2
            print("Bölüm: ", result)
    else:
        print("Geçersiz seçim. Lütfen tekrar deneyin.")
