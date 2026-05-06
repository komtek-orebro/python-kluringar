# Extra utmaningar

Har du gjort klart grunduppgifterna? Här kan du välja din egen väg beroende på vad du tycker är roligast.
Välj det spår som lockar mest — eller gör båda!

---

## 🔢 Spår A — Matematik & Former

> Perfekt om du gillar matte, mönster och logik. Här bygger du figurer med loopar och löser matteproblem med kod.

---

### M1 — Bygg en linje [📄 exempel](https://github.com/komtek-orebro/python-kluringar/blob/main/exempel/matematik/m1_linje.py)

Låt användaren skriva in ett tal `n`. Skriv ut en horisontell linje av `n` stycken `*`.

**Exempel (`n = 6`):**
```
******
```

<details markdown="1">
<summary>💡 Tips om du fastnar</summary>

Du kan multiplicera en `string` med ett tal i Python för att upprepa den:

```python
print("*" * n)
```

</details>

---

### M2 — Bygg en rektangel [📄 exempel](https://github.com/komtek-orebro/python-kluringar/blob/main/exempel/matematik/m2_rektangel.py)

Låt användaren skriva in bredd och höjd. Skriv ut en rektangel av `*`.

**Exempel (bredd `5`, höjd `3`):**
```
*****
*****
*****
```

<details markdown="1">
<summary>💡 Tips om du fastnar</summary>

Använd en `for`-loop som loopar `höjd` gånger, och skriv ut en rad på `bredd` stjärnor varje varv:

```python
for i in range(höjd):
    print("*" * bredd)
```

</details>

---

### M3 — Bygg en triangel [📄 exempel](https://github.com/komtek-orebro/python-kluringar/blob/main/exempel/matematik/m3_triangel.py)

Låt användaren skriva in ett tal `n`. Skriv ut en triangel av `*` med `n` rader, där rad 1 har en stjärna, rad 2 har två, osv.

**Exempel (`n = 5`):**
```
*
**
***
****
*****
```

<details markdown="1">
<summary>💡 Tips om du fastnar</summary>

I en `for`-loop med `range(1, n+1)` är loop-variabeln `i` på rad 1 lika med `1`, på rad 2 lika med `2`, osv. Skriv ut `"*" * i` varje varv.

</details>

---

### M4 — Bygg en pyramid [📄 exempel](https://github.com/komtek-orebro/python-kluringar/blob/main/exempel/matematik/m4_pyramid.py)

Bygg vidare på triangeln — den här gången ska pyramiden vara centrerad med mellanslag på sidorna.

**Exempel (`n = 5`):**
```
    *
   ***
  *****
 *******
*********
```

<details markdown="1">
<summary>💡 Tips om du fastnar</summary>

På rad `i` (börja från 1) behöver du:
- `n - i` mellanslag på vänster sida
- `2 * i - 1` stjärnor i mitten

```python
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))
```

</details>

---

### M5 — Primtalscheck [📄 exempel](https://github.com/komtek-orebro/python-kluringar/blob/main/exempel/matematik/m5_primtal.py)

Låt användaren skriva in ett tal och kontrollera om det är ett primtal (ett tal som bara är delbart med 1 och sig självt).

**Exempel:**
```
Skriv ett tal: 17
17 är ett primtal!
```
```
Skriv ett tal: 12
12 är inte ett primtal. (delbart med 2)
```

<details markdown="1">
<summary>💡 Tips om du fastnar</summary>

Loopa igenom alla tal från `2` upp till (men inte inklusive) ditt tal. Om något av dem delar ditt tal jämnt (använd `%`), är det inte ett primtal. Tal som är `1` eller lägre är aldrig primtal.

```python
är_primtal = True
for i in range(2, tal):
    if tal % i == 0:
        är_primtal = False
        break
```

</details>

---

### M6 — Temperaturomvandlare [📄 exempel](https://github.com/komtek-orebro/python-kluringar/blob/main/exempel/matematik/m6_temperatur.py)

Bygg ett program som omvandlar temperaturer. Låt användaren välja riktning (Celsius → Fahrenheit eller tvärtom) och mata in ett värde.

Formlerna är:
- Celsius till Fahrenheit: `F = C * 9/5 + 32`
- Fahrenheit till Celsius: `C = (F - 32) * 5/9`

**Exempel:**
```
Välj riktning:
1. Celsius till Fahrenheit
2. Fahrenheit till Celsius
Val: 1
Temperatur i Celsius: 100
100°C = 212.0°F
```

<details markdown="1">
<summary>💡 Tips om du fastnar</summary>

Använd `round()` för att avrunda resultatet till ett lagom antal decimaler:

```python
resultat = round(C * 9/5 + 32, 1)
```

</details>

---

### M7 — Fibonacci-sekvensen [📄 exempel](https://github.com/komtek-orebro/python-kluringar/blob/main/exempel/matematik/m7_fibonacci.py)

Skriv ett program som genererar de första `n` talen i Fibonacci-sekvensen. Varje tal är summan av de två föregående (0, 1, 1, 2, 3, 5, 8, 13, ...).

**Exempel (`n = 8`):**
```
0 1 1 2 3 5 8 13
```

<details markdown="1">
<summary>💡 Tips om du fastnar</summary>

Spara de två senaste talen i variabler och uppdatera dem i varje varv av loopen:

```python
a, b = 0, 1
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
```

`a, b = b, a + b` byter värden på ett smidigt sätt — `a` får `b`:s gamla värde, och `b` får summan.

</details>

---

## 📝 Spår B — Strängar & Text

> Perfekt om du gillar ord, språk och kreativa lösningar. Här manipulerar du text på olika sätt.

---

### S1 — Vänd på en mening [📄 exempel](https://github.com/komtek-orebro/python-kluringar/blob/main/exempel/strängar/s1_vänd.py)

Låt användaren skriva in ett ord eller en mening och skriv ut det baklänges.

**Exempel:**
```
Skriv något: hejsan
Baklänges: nasejh
```

<details markdown="1">
<summary>💡 Tips om du fastnar</summary>

I Python kan du vända en `string` med `slice`-notation. `text[::-1]` betyder "hela texten, baklänges":

```python
baklänges = text[::-1]
```

</details>

---

### S2 — Räkna vokaler [📄 exempel](https://github.com/komtek-orebro/python-kluringar/blob/main/exempel/strängar/s2_vokaler.py)

Låt användaren skriva in en mening. Räkna och skriv ut hur många vokaler (a, e, i, o, u, å, ä, ö) det finns.

**Exempel:**
```
Skriv en mening: Hej världen!
Antal vokaler: 4
```

<details markdown="1">
<summary>💡 Tips om du fastnar</summary>

Loopa igenom varje bokstav i texten och kontrollera om den finns i en `string` med alla vokaler. Använd `.lower()` för att hantera stora och små bokstäver lika:

```python
vokaler = "aeiouåäö"
antal = 0
for bokstav in text.lower():
    if bokstav in vokaler:
        antal += 1
```

</details>

---

### S3 — Palindromkontroll [📄 exempel](https://github.com/komtek-orebro/python-kluringar/blob/main/exempel/strängar/s3_palindrom.py)

Skriv ett program som kontrollerar om ett ord är ett **palindrom** — det vill säga om det läses likadant framifrån och bakifrån (t.ex. "racecar", "level", "madam").

**Exempel:**
```
Skriv ett ord: racecar
'racecar' är ett palindrom!
```
```
Skriv ett ord: python
'python' är inte ett palindrom.
```

<details markdown="1">
<summary>💡 Tips om du fastnar</summary>

Kombinera tips från S1 — jämför ordet med sig självt baklänges. Använd `.lower()` så att stora och små bokstäver inte spelar roll.

</details>

---

### S4 — Ordräknare [📄 exempel](https://github.com/komtek-orebro/python-kluringar/blob/main/exempel/strängar/s4_ordräknare.py)

Låt användaren skriva in en mening. Skriv ut hur många ord meningen innehåller, och vilket ord som är längst.

**Exempel:**
```
Skriv en mening: Jag älskar att programmera i Python
Antal ord: 6
Längsta ordet: programmera (11 bokstäver)
```

<details markdown="1">
<summary>💡 Tips om du fastnar</summary>

Använd `.split()` för att dela upp en `string` i en `list` av ord (den delar på mellanslag automatiskt):

```python
ord = mening.split()
antal = len(ord)
```

För att hitta det längsta ordet kan du loopa igenom listan och jämföra längder med `len()`.

</details>

---

### S5 — Caesar-chiffer [📄 exempel](https://github.com/komtek-orebro/python-kluringar/blob/main/exempel/strängar/s5_caesar.py)

Bygg ett enkelt krypteringsprogram! Låt användaren skriva in en mening och ett förskjutningsvärde (t.ex. 3). Flytta varje bokstav i alfabetet med det antalet steg framåt. `a` blir `d`, `b` blir `e`, osv.

**Exempel (förskjutning `3`):**
```
Skriv en mening: hej
Krypterat: khm
```

<details markdown="1">
<summary>💡 Tips om du fastnar</summary>

`ord()` ger dig ett teckens sifferkod och `chr()` omvandlar tillbaka. Bokstäverna `a`–`z` har koderna 97–122. Använd `%` för att "wrappa" runt alfabetet:

```python
ny_bokstav = chr((ord(bokstav) - ord('a') + förskjutning) % 26 + ord('a'))
```

Hoppa över tecken som inte är bokstäver (mellanslag, utropstecken osv.).

</details>

---

### S6 — Textstatistik [📄 exempel](https://github.com/komtek-orebro/python-kluringar/blob/main/exempel/strängar/s6_statistik.py)

Bygg ett program som analyserar en text som användaren skriver in och visar:
- Antal tecken (med och utan mellanslag)
- Antal ord
- Antal meningar (räkna `.`, `!` och `?`)
- Vanligaste bokstaven

**Exempel:**
```
Skriv en text: Hej! Jag heter Anna. Vad heter du?
Tecken (med mellanslag): 38
Tecken (utan mellanslag): 31
Antal ord: 7
Antal meningar: 3
Vanligaste bokstaven: e (4 gånger)
```

<details markdown="1">
<summary>💡 Tips om du fastnar</summary>

- Antal tecken utan mellanslag: `text.replace(" ", "")` tar bort alla mellanslag.
- Räkna meningar: loopa igenom texten och kolla om varje tecken är `.`, `!` eller `?`.
- Vanligaste bokstaven: skapa en `dictionary` där varje bokstav är en nyckel och värdet är hur många gånger den förekommer. Använd sedan `max()` för att hitta den med högst värde.

</details>

---

## Klarat båda spåren?

Prova att kombinera dem! Här är ett par idéer:

| Utmaning | Beskrivning |
|----------|-------------|
| **Kombinera M5 + S1** | Skriv ut alla primtal upp till 100 i omvänd ordning |
| **Kombinera M3 + S1** | Bygg en triangel av ett ord — rad 1: `P`, rad 2: `Py`, rad 3: `Pyt`, osv. |
| **Kombinera M6 + S6** | Bygg en fullständig "konverteringsapp" där användaren kan konvertera temperaturer och samtidigt visa statistik om sina inmatningar |
