# M6 — Temperaturomvandlare
# Omvandla mellan Celsius och Fahrenheit.

print("Välj riktning:")
print("1. Celsius till Fahrenheit")
print("2. Fahrenheit till Celsius")

val = input("Val: ")

if val == "1":
    celsius = float(input("Temperatur i Celsius: "))
    fahrenheit = round(celsius * 9 / 5 + 32, 1)
    print(f"{celsius}°C = {fahrenheit}°F")
elif val == "2":
    fahrenheit = float(input("Temperatur i Fahrenheit: "))
    celsius = round((fahrenheit - 32) * 5 / 9, 1)
    print(f"{fahrenheit}°F = {celsius}°C")
else:
    print("Ogiltigt val.")
