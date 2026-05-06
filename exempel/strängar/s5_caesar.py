# S5 — Caesar-chiffer
# Kryptera en mening genom att flytta varje bokstav ett antal steg i alfabetet.

mening = input("Skriv en mening: ")
förskjutning = int(input("Hur många steg vill du förskjuta? "))

krypterad = ""
for tecken in mening:
    if tecken.isalpha():
        bas = ord('A') if tecken.isupper() else ord('a')
        ny_bokstav = chr((ord(tecken) - bas + förskjutning) % 26 + bas)
        krypterad += ny_bokstav
    else:
        krypterad += tecken

print(f"Krypterat: {krypterad}")
