# S3 — Palindromkontroll
# Kontrollera om ett ord läses likadant framifrån och bakifrån.

ord = input("Skriv ett ord: ").lower()

if ord == ord[::-1]:
    print(f"'{ord}' är ett palindrom!")
else:
    print(f"'{ord}' är inte ett palindrom.")
