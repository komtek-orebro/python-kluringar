# S2 — Räkna vokaler
# Räkna hur många vokaler en mening innehåller.

mening = input("Skriv en mening: ")
vokaler = "aeiouåäö"
antal = 0

for bokstav in mening.lower():
    if bokstav in vokaler:
        antal += 1

print(f"Antal vokaler: {antal}")
