import pyshorteners

# URL original #
url = 'https://www.instagram.com/muriloolegini/'

# Carrega lib #
s = pyshorteners.Shortener()

# Gera URL encurtada #
shortUrl = s.tinyurl.short(url)

# Mostra resultado #
print(f"URL Encurtada: {shortUrl}")
