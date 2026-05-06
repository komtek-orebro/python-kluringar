# Uppgift 12 — Multiplikationstabell
# Skriv ut multiplikationstabellen för ett tal som användaren väljer.

tal = int(input("Vilket tal vill du ha tabellen för? "))

for i in range(1, 11):
    print(f"{tal} * {i} = {tal * i}")
