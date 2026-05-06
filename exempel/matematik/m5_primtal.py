# M5 — Primtalscheck
# Kontrollera om ett tal som användaren skriver in är ett primtal.

tal = int(input("Skriv ett tal: "))

if tal <= 1:
    print(f"{tal} är inte ett primtal.")
else:
    är_primtal = True
    for i in range(2, tal):
        if tal % i == 0:
            är_primtal = False
            print(f"{tal} är inte ett primtal. (delbart med {i})")
            break

    if är_primtal:
        print(f"{tal} är ett primtal!")
