# Uppgift 10 — Jämna och udda tal
# Skriv ut alla jämna tal och alla udda tal från 1 till 20, på varsin rad.

print("Jämna:", end=" ")
for i in range(2, 21, 2):
    print(i, end=" ")

print()  # Ny rad

print("Udda:", end=" ")
for i in range(1, 20, 2):
    print(i, end=" ")

print()  # Ny rad
