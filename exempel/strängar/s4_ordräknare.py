# S4 — Ordräknare
# Räkna ord i en mening och hitta det längsta.

mening = input("Skriv en mening: ")
ord = mening.split()
antal = len(ord)

längsta = ""
for o in ord:
    if len(o) > len(längsta):
        längsta = o

print(f"Antal ord: {antal}")
print(f"Längsta ordet: {längsta} ({len(längsta)} bokstäver)")
