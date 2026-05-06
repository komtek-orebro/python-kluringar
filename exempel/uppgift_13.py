# Uppgift 13 — Tärning
# Simulera ett tärningskast och låt användaren kasta igen så många gånger de vill.

import random

fortsätt = True
while fortsätt:
    resultat = random.randint(1, 6)
    print(f"Du slog: {resultat}")

    svar = input("Vill du kasta igen? (ja/nej): ")
    if svar.lower() == "nej":
        fortsätt = False

print("Hej då!")
