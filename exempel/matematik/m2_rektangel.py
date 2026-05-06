# M2 — Bygg en rektangel
# Skriv ut en rektangel av * med en bredd och höjd som användaren väljer.

bredd = int(input("Hur bred ska rektangeln vara? "))
höjd = int(input("Hur hög ska rektangeln vara? "))

for i in range(höjd):
    print("*" * bredd)
