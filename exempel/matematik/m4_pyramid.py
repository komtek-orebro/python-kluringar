# M4 — Bygg en pyramid
# Skriv ut en centrerad pyramid av * med n rader.

n = int(input("Hur många rader ska pyramiden ha? "))

for i in range(1, n + 1):
    mellanslag = " " * (n - i)
    stjärnor = "*" * (2 * i - 1)
    print(mellanslag + stjärnor)
