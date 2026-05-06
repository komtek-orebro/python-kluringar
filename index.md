# Python-kluringar 🐍

Välkommen! Det här är en samling uppgifter för dig som vill lära dig programmera i Python.
Du behöver inte kunna något sedan tidigare — vi börjar från allra början och ökar svårighetsgraden steg för steg.

**Hur du kör din kod:** Öppna en terminal, navigera till mappen där din fil ligger och skriv `python filnamn.py`.

---

## Nivå 1 — Kom igång

> Här lär du dig de absolut grundläggande byggstenarna: hur du skriver ut text och hur du tar emot information från användaren.

---

### Uppgift 1 — Hej världen [📄 exempel](exempel/uppgift_01.py)

Skriv ett program som skriver ut ditt namn i konsolen.

**Förväntat resultat:**

```
Förnamn Efternamn
```

<details markdown="1">
<summary>💡 Tips om du fastnar</summary>

Använd funktionen `print()` för att skriva ut text. Text som ska skrivas ut bokstavligt omges av citattecken:

```python
print("Det här är text")
```

</details>

---

### Uppgift 2 — Ta emot input [📄 exempel](exempel/uppgift_02.py)

Låt användaren skriva in sitt namn och skriv sedan ut `Hej {namn}!`.

**Exempel:**

```
Vad heter du?
> Anna
Hej Anna!
```

<details markdown="1">
<summary>💡 Tips om du fastnar</summary>

Funktionen `input()` pausar programmet och väntar på att användaren ska skriva något. Det användaren skriver sparas i en `variable`:

```python
svar = input("Vad heter du? ")
print("Hej", svar)
```

</details>

---

### Uppgift 3 — Förnamn och efternamn [📄 exempel](exempel/uppgift_03.py)

Låt användaren skriva in sitt förnamn och efternamn i två separata steg. Skriv sedan ut `Hej {förnamn} {efternamn}!`.

**Exempel:**

```
Vad är ditt förnamn?
> Anna
Vad är ditt efternamn?
> Svensson
Hej Anna Svensson!
```

<details markdown="1">
<summary>💡 Tips om du fastnar</summary>

Du kan kombinera flera `variables` i ett `print()`-anrop genom att separera dem med kommatecken:

```python
print("Hej", förnamn, efternamn)
```

</details>

---

## Nivå 2 — Matematik

> Nu introducerar vi siffror och enkla räkneoperationer. En viktig sak att veta är att `input()` alltid returnerar text (`string`), inte ett tal. För att kunna räkna med det måste du omvandla det till ett heltal med `int()`.

---

### Uppgift 4 — Summera två tal [📄 exempel](exempel/uppgift_04.py)

Låt användaren skriva in två tal och skriv sedan ut summan av dem.

**Exempel:**

```
Skriv ett tal: 5
Skriv ett till tal: 3
Summan är: 8
```

<details markdown="1">
<summary>💡 Tips om du fastnar</summary>

`input()` ger alltid tillbaka text, inte ett tal. Prova vad som händer om du skriver `"5" + "3"` — du får `"53"`, inte `8`! Använd `int()` för att omvandla texten till ett heltal innan du räknar:

```python
tal = int(input("Skriv ett tal: "))
```

</details>

---

### Uppgift 5 — Miniräknare [📄 exempel](exempel/uppgift_05.py)

Bygg vidare på uppgift 4. Låt användaren skriva in två tal och skriv sedan ut resultatet av **alla** fyra räknesätt: addition (`+`), subtraktion (`-`), multiplikation (`*`) och division (`/`).

**Exempel:**

```
Skriv ett tal: 10
Skriv ett till tal: 4
10 + 4 = 14
10 - 4 = 6
10 * 4 = 40
10 / 4 = 2.5
```

<details markdown="1">
<summary>💡 Tips om du fastnar</summary>

Du kan blanda text och variabler i `print()` med hjälp av ett `f-string`. Skriv `f` precis före citattecknet och sätt variabelnamn inom klamrar `{}`:

```python
print(f"{tal1} + {tal2} = {tal1 + tal2}")
```

</details>

---

## Nivå 3 — Beslut med if/else

> Program behöver kunna ta beslut beroende på vad som händer. Det gör vi med `if` och `else`. Tänk på det som: _"Om det här stämmer, gör såhär — annars gör såhär."_

---

### Uppgift 6 — Större eller mindre [📄 exempel](exempel/uppgift_06.py)

Låt användaren skriva in ett tal. Skriv ut om talet är **positivt**, **negativt** eller **noll**.

**Exempel:**

```
Skriv ett tal: -7
Det talet är negativt!
```

<details markdown="1">
<summary>💡 Tips om du fastnar</summary>

Använd `if`, `elif` (else if) och `else` för att kontrollera flera villkor:

```python
if tal > 0:
    print("Positivt")
elif tal < 0:
    print("Negativt")
else:
    print("Noll")
```

Glöm inte att det ska vara ett kolon (`:`) i slutet av varje `if`/`elif`/`else`-rad, och att koden inuti måste vara indragen (4 mellanslag eller ett tab).

</details>

---

### Uppgift 7 — Mopedkörkortet [📄 exempel](exempel/uppgift_07.py)

Låt användaren skriva in sin ålder. Om personen är 15 år eller äldre, skriv ut att de får köra moped. Annars, skriv ut hur många år det är kvar tills de fyller 15.

**Exempel:**

```
Hur gammal är du? 12
Du behöver vänta 3 år till.
```

```
Hur gammal är du? 17
Du får köra moped!
```

<details markdown="1">
<summary>💡 Tips om du fastnar</summary>

För att räkna ut hur många år det är kvar kan du subtrahera:

```python
år_kvar = 15 - ålder
```

Kom ihåg att omvandla åldern från text till heltal med `int()`.

</details>

---

### Uppgift 8 — Jämnt eller udda [📄 exempel](exempel/uppgift_08.py)

Låt användaren skriva in ett tal och skriv ut om det är jämnt eller udda.

**Exempel:**

```
Skriv ett tal: 7
7 är ett udda tal.
```

<details markdown="1">
<summary>💡 Tips om du fastnar</summary>

Operatorn `%` (modulo) ger resten vid heltalsdivision. `7 % 2` ger `1` (eftersom 7 delat med 2 ger resten 1). Om `tal % 2 == 0` är talet jämnt, annars är det udda.

</details>

---

## Nivå 4 — Loopar

> En `loop` låter dig upprepa kod många gånger utan att behöva skriva samma sak om och om igen. Det finns två vanliga sorters loopar: `for` (när du vet hur många gånger du vill loopa) och `while` (när du vill loopa så länge ett villkor stämmer).

---

### Uppgift 9 — Räkna till tio [📄 exempel](exempel/uppgift_09.py)

Skriv ett program som skriver ut talen 1 till och med 10, ett tal per rad.

**Förväntat resultat:**

```
1
2
3
...
10
```

<details markdown="1">
<summary>💡 Tips om du fastnar</summary>

Använd en `for`-loop med `range()`. Observera att `range(10)` ger talen 0–9, inte 1–10. Du kan antingen börja räkna från 1 med `range(1, 11)`, eller lägga till 1 på varje tal:

```python
for i in range(1, 11):
    print(i)
```

</details>

---

### Uppgift 10 — Jämna och udda tal [📄 exempel](exempel/uppgift_10.py)

Skriv ut alla **jämna** tal från 1 till 20 på en rad, och alla **udda** tal från 1 till 20 på en annan rad.

**Förväntat resultat:**

```
Jämna: 2 4 6 8 10 12 14 16 18 20
Udda: 1 3 5 7 9 11 13 15 17 19
```

<details markdown="1">
<summary>💡 Tips om du fastnar</summary>

Du kan använda `range()` med tre argument: start, stop och steg. `range(2, 21, 2)` ger alla jämna tal från 2 till 20.

För att skriva ut alla tal på en och samma rad, använd parametern `end` i `print()`:

```python
print(tal, end=" ")
```

Alternativt kan du samla talen i en `string` och skriva ut den efteråt.

</details>

---

### Uppgift 11 — Summera tal [📄 exempel](exempel/uppgift_11.py)

Skriv ett program som adderar alla heltal från 1 till och med 100 och skriver ut det totala resultatet.

**Förväntat resultat:**

```
Summan av 1 till 100 är: 5050
```

<details markdown="1">
<summary>💡 Tips om du fastnar</summary>

Skapa en `variable` som börjar på 0 och lägg till varje tal i loopen:

```python
summa = 0
for i in range(1, 101):
    summa = summa + i
print(summa)
```

</details>

---

### Uppgift 12 — Multiplikationstabell [📄 exempel](exempel/uppgift_12.py)

Låt användaren skriva in ett tal och skriv sedan ut multiplikationstabellen för det talet (1–10).

**Exempel:**

```
Vilket tal vill du ha tabellen för? 7
7 * 1 = 7
7 * 2 = 14
...
7 * 10 = 70
```

<details markdown="1">
<summary>💡 Tips om du fastnar</summary>

Använd en `for`-loop från 1 till 11 och multiplicera användarens tal med loop-variabeln. Använd ett `f-string` för att formatera utskriften snyggt.

</details>

---

## Nivå 5 — Kombinera allt

> Dags att sätta ihop vad du lärt dig! De här uppgifterna kräver att du kombinerar `variables`, `input`, `if/else` och `loops`.

---

### Uppgift 13 — Tärning [📄 exempel](exempel/uppgift_13.py)

Skriv ett program som simulerar ett tärningskast (ett tal mellan 1 och 6). Fråga sedan användaren om de vill kasta igen, och fortsätt tills de svarar nej.

**Exempel:**

```
Du slog: 4
Vill du kasta igen? (ja/nej): ja
Du slog: 1
Vill du kasta igen? (ja/nej): nej
Hej då!
```

<details markdown="1">
<summary>💡 Tips om du fastnar</summary>

Importera modulen `random` och använd `random.randint(1, 6)` för att generera ett slumpmässigt tal. En `while`-loop med en `boolean` (`True`/`False`) är bra här:

```python
import random

fortsätt = True
while fortsätt:
    resultat = random.randint(1, 6)
    print("Du slog:", resultat)
    svar = input("Vill du kasta igen? (ja/nej): ")
    if svar.lower() == "nej":
        fortsätt = False
```

</details>

---

### Uppgift 14 — Gissa talet [📄 exempel](exempel/uppgift_14.py)

Datorn väljer ett hemligt tal mellan 1 och 20. Användaren får gissa vilket tal det är. Efter varje gissning ska programmet säga om gissningen var för hög, för låg, eller rätt. Användaren har max 5 försök.

**Exempel:**

```
Gissa ett tal mellan 1 och 20!
Gissning 1/5: 10
För lågt!
Gissning 2/5: 15
För högt!
Gissning 3/5: 13
Rätt! Du klarade det på 3 försök.
```

<details markdown="1">
<summary>💡 Tips om du fastnar</summary>

- Generera det hemliga talet med `random.randint(1, 20)` **utanför** loopen.
- Håll koll på antalet försök med en räknare (`counter`).
- Använd `break` för att avsluta loopen direkt när användaren gissar rätt.
- Kontrollera efter loopen om de tog slut på försök.

</details>

---

### Uppgift 15 — Sten, sax, påse [📄 exempel](exempel/uppgift_15.py)

Bygg ett sten-sax-påse-spel mot datorn! Spelaren skriver in sitt val, datorn väljer slumpmässigt, och programmet avgör vem som vinner. Håll koll på poängen och fortsätt spela tills spelaren väljer att sluta.

**Exempel:**

```
Välj (sten/sax/påse) eller 'sluta': sten
Datorn valde: sax
Du vann! Poäng — Du: 1, Datorn: 0

Välj (sten/sax/påse) eller 'sluta': påse
Datorn valde: påse
Oavgjort! Poäng — Du: 1, Datorn: 0

Välj (sten/sax/påse) eller 'sluta': sluta
Slutresultat — Du: 1, Datorn: 0
```

<details markdown="1">
<summary>💡 Tips om du fastnar</summary>

- Spara valen i en `list`: `val = ["sten", "sax", "påse"]` och använd `random.choice(val)` för datorns val.
- Rita upp vinnartabellen för dig själv: sten slår sax, sax slår påse, påse slår sten.
- Skapa separata `variables` för spelarens och datorns poäng och uppdatera dem i loopen.
- Validera spelarens input — om de skriver något ogiltigt, be dem försöka igen.

</details>

---

## Välj ditt spår

Har du klarat grunduppgifterna? Gå vidare till **[EXTRA-UTMANINGAR.md](EXTRA-UTMANINGAR.md)** där du kan välja spår beroende på vad du gillar mest:

- **🔢 Spår A — Matematik & Former** — Bygg figurer med loopar, kolla primtal, generera Fibonacci-sekvenser och mer
- **📝 Spår B — Strängar & Text** — Vänd meningar, kryptera text, analysera ord och mer

---

## Bonusutmaningar

Har du klarat allt ovan? Här är lite extra utmaningar för dig som vill ha mer!

| #   | Uppgift                                                                                                                                                           | Svårighet |
| --- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------- |
| B1  | Bygg ett program som kontrollerar om ett ord är ett **palindrom** (läses likadant framifrån och bakifrån, t.ex. "racecar")                                        | ⭐⭐      |
| B2  | Skriv ett program som räknar hur många **vokaler** det finns i en mening som användaren skriver in                                                                | ⭐⭐      |
| B3  | Gör ett **FizzBuzz**-program: skriv ut talen 1–100, men ersätt multipler av 3 med "Fizz", multipler av 5 med "Buzz", och multipler av både 3 och 5 med "FizzBuzz" | ⭐⭐      |
| B4  | Bygg ett **lösenordsgenerator**-program som skapar ett slumpmässigt lösenord baserat på en längd som användaren väljer                                            | ⭐⭐⭐    |
| B5  | Bygg ett **hänga gubben**-spel i terminalen                                                                                                                       | ⭐⭐⭐⭐  |

---

_Lycka till och kom ihåg — alla programmerare googlar och gör fel. Det är så man lär sig!_
