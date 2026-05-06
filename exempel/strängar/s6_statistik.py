# S6 — Textstatistik
# Analysera en text och visa statistik om den.

text = input("Skriv en text: ")

tecken_med_mellanslag = len(text)
tecken_utan_mellanslag = len(text.replace(" ", ""))

ord = text.split()
antal_ord = len(ord)

antal_meningar = 0
for tecken in text:
    if tecken in ".!?":
        antal_meningar += 1

bokstavsfrekvens = {}
for bokstav in text.lower():
    if bokstav.isalpha():
        if bokstav in bokstavsfrekvens:
            bokstavsfrekvens[bokstav] += 1
        else:
            bokstavsfrekvens[bokstav] = 1

vanligaste = max(bokstavsfrekvens, key=bokstavsfrekvens.get)

print(f"Tecken (med mellanslag): {tecken_med_mellanslag}")
print(f"Tecken (utan mellanslag): {tecken_utan_mellanslag}")
print(f"Antal ord: {antal_ord}")
print(f"Antal meningar: {antal_meningar}")
print(f"Vanligaste bokstaven: {vanligaste} ({bokstavsfrekvens[vanligaste]} gånger)")
