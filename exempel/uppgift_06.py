# Uppgift 6 — Större eller mindre
# Låt användaren skriva in ett tal och skriv ut om det är positivt, negativt eller noll.

tal = int(input("Skriv ett tal: "))

if tal > 0:
    print(f"{tal} är ett positivt tal!")
elif tal < 0:
    print(f"{tal} är ett negativt tal!")
else:
    print("Du skrev in noll!")
