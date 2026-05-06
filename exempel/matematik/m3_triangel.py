# M3 — Bygg en triangel
# Skriv ut en triangel av * med n rader.

n = int(input("Hur många rader ska triangeln ha? "))

for i in range(1, n + 1):
    print("*" * i)
