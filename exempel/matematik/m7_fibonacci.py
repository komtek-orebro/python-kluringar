# M7 — Fibonacci-sekvensen
# Generera de första n talen i Fibonacci-sekvensen.

n = int(input("Hur många tal vill du ha? "))

a, b = 0, 1
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b

print()  # Ny rad efter alla tal
