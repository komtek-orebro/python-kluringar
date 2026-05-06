# Uppgift 15 — Sten, sax, påse
# Spela sten-sax-påse mot datorn och håll koll på poängen.

import random

val = ["sten", "sax", "påse"]
spelar_poäng = 0
dator_poäng = 0

while True:
    spelar_val = input("\nVälj (sten/sax/påse) eller 'sluta': ").lower()

    if spelar_val == "sluta":
        break

    if spelar_val not in val:
        print("Ogiltigt val! Skriv 'sten', 'sax' eller 'påse'.")
        continue

    dator_val = random.choice(val)
    print(f"Datorn valde: {dator_val}")

    if spelar_val == dator_val:
        print("Oavgjort!")
    elif (
        (spelar_val == "sten" and dator_val == "sax")
        or (spelar_val == "sax" and dator_val == "påse")
        or (spelar_val == "påse" and dator_val == "sten")
    ):
        print("Du vann!")
        spelar_poäng += 1
    else:
        print("Datorn vann!")
        dator_poäng += 1

    print(f"Poäng — Du: {spelar_poäng}, Datorn: {dator_poäng}")

print(f"\nSlutresultat — Du: {spelar_poäng}, Datorn: {dator_poäng}")
