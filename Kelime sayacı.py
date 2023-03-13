import requests
from bs4 import BeautifulSoup

# Kullanıcıdan bir seçenek iste
option = input("Metin belgesi için '1', URL için '2' girin: ")

# Metin belgesi seçeneği
if option == "1":
    # Kullanıcıdan metin belgesinin yolunu iste
    file_path = input("Metin belgesinin yolunu girin: ")
    
    # Metin belgesini aç ve oku
    with open(file_path, 'r') as file:
        text = file.read()
    
    # Kelime sayısını bul
    word_count = len(text.split())
    print("Belgedeki kelime sayısı:", word_count)

# URL seçeneği
elif option == "2":
    # Kullanıcıdan URL'yi iste
    url = input("URL'yi girin: ")
    
    # Sayfayı indir ve oku
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    
    # Metni bul ve kelime sayısını bul
    text = soup.get_text()
    word_count = len(text.split())
    print("Belgedeki kelime sayısı:", word_count)

# Geçersiz seçenek
else:
    print("Geçersiz seçenek!")
