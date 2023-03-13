import pyshorteners

url = input("Enter the URL to be shortened: ")

# Create an instance of the Shortener class
s = pyshorteners.Shortener()

# Shorten the URL using the TinyURL service
short_url = s.tinyurl.short(url)

print("Shortened URL:", short_url)
