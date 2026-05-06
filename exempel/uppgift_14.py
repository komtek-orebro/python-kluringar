# Uppgift 14 — Gissa talet
# Datorn väljer ett hemligt tal mellan 1 och 20. Användaren har 5 försök att gissa rätt.

import random

hemligt_tal = random.randint(1, 20)
max_försök = 5

print("Gissa ett tal mellan 1 och 20!")

for försök in range(1, max_försök + 1):
    gissning = int(input(f"Gissning {försök}/{max_försök}: "))

    if gissning == hemligt_tal:
        print(f"Rätt! Du klarade det på {försök} försök.")
        break
    elif gissning < hemligt_tal:
        print("För lågt!")
    else:
        print("För högt!")

    if försök == max_försök:
        print(f"Tyvärr, du fick inga fler försök. Det hemliga talet var {hemligt_tal}.")
