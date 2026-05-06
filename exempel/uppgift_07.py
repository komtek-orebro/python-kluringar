# Uppgift 7 — Mopedkörkortet
# Kontrollera om användaren är gammal nog att köra moped (15 år).

ålder = int(input("Hur gammal är du? "))
åldersgräns = 15

if ålder >= åldersgräns:
    print("Du får köra moped!")
else:
    år_kvar = åldersgräns - ålder
    print(f"Du behöver vänta {år_kvar} år till.")
