#1 Skriv ut ditt namn i konsollen
print("Jonatan Berg")

#2 Låt användaren skriva in sitt namn, och skriv sedan ut "Hej {namn}"
name = input("Vad heter du?\n")
print("Hej", name)

#3 Låt användaren skriva in sitt förnamn först och sedan sitt efternamn. Skriv sedan ut "Hej {förnamn} {efternamn}"
firstname = input("Vad är ditt förnamn?\n")
lastname = input("Och vad är ditt efternamn?\n")
print("Hej", firstname, lastname)

#4 Låt användaren skriva in två tal, skriv sedan ut summan (+) av de två talen
number_one = input("Skriv ett tal\n")
number_two = input("Skriv ett annat tal\n")
sum = int(number_one) + int(number_two)
print("Summan av", number_one, "och", number_two, "är", sum)

#5 Skriv ut talen 1 -> 10
for i in range(10):
    print(i+1)


#6 Skriv ut alla jämna tal mellan 1 och 10
for i in range(5):
    print((i+1)*2)


#7 Skriv ut alla ojämna tal mellan 1 och 10
for i in range(5):
    print((i*2)+1)

#8 Addera alla tal mellan 1 och 10 och skriv ut summan
sum = 0
for i in range(10):
    sum = sum + (i+1)

print(sum)

#9 Låt användaren skriva in ett tal. Om talet är lika med eller större än 15 så skriv ut att användaren får åka moped. Om talet är lägre än 15 så skriv ut att användaren inte får åka moped.
age_limit = int(15)
age = int(input("Hur gammal är du?\n"))
print("Du får åka moped") if age > age_limit else print("Du får inte åka moped")

#10 Sten-sax-påse mot datorn
import random

# 0 = sten
# 1 = sax
# 2 = påse

keep_going = True
opponent = random.randint(0,2)

while keep_going:
    keep_going = False
    player = input("Spelar du 'Sten', 'Sax', eller 'Påse'?\n")

    if player.lower() == "sten":
        if opponent == 0:
            print("Båda valde sten, oavgjort!")
        elif opponent == 1:
            print("Datorn valde sax, du vann!")
        elif opponent == 2:
            print("Datorn valde påse, du förlorade!")
    elif player.lower() == "sax":
        if opponent == 0:
            print("Datorn valde sten, du förlorade!")
        elif opponent == 1:
            print("Datorn valde sax, oavgjort!")
        elif opponent == 2:
            print("Datorn valde påse, du vann!")
    elif player.lower() == "påse":
        if opponent == 0:
            print("Datorn valde sten, du vann!")
        elif opponent == 1:
            print("Datorn valde sax, du förlorade!")
        elif opponent == 2:
            print("Datorn valde påse, oavgjort!")
    else:
        print("Ogiltigt val")
        keep_going = True

#11 Hänga gubbe


#12 Dynamisk tärning
import random

low = int(input("Vad är det nedre intervallet?\n"))
high = 0
valid = False
while valid == False:
    high = int(input("Vad är det övre intervallet?\n"))
    if low > high:
        print("Det övre intervallet måste vara större än det lägre")
    else:
        valid = True

keep_going = True
while keep_going:
    result = random.randint(low, high)
    print(result)
    valid_input = False
    response = ""
    while valid_input == False:
        response = input("Vill du köra igen? (JA/NEJ)")
        if response.lower() == "ja" or response.lower() == "nej":
            valid_input = True
        else:
            print("Felaktig input. Du måste svara 'JA' eller 'NEJ'.")
    if response.lower() == "nej":
        keep_going = False


#13 Gissa-siffran-spel
import random

low = int(input("Vad är det nedre intervallet?\n"))
high = 0
valid = False
while valid == False:
    high = int(input("Vad är det övre intervallet?\n"))
    if low > high:
        print("Det övre intervallet måste vara större än det lägre")
    else:
        valid = True

correct_number = random.randint(low, high)

guesses = 0
max_guesses = 5

while guesses < max_guesses:
    guess = int(input("Vilken siffra gissar du på?\n"))
    if guess == correct_number:
        print("Grattis! Du gissade rätt efter", guesses + 1, "försök.")
        break
    elif guess < correct_number:
        print("Du gissade för lågt.")
    elif guess > correct_number:
        print("Du gissade för högt.")
    
    guesses = guesses + 1
    if guesses == max_guesses:
        print("Du har gissat max antal gånger. Rätt nummber var", correct_number)
    else:
        print(f"Du har försökt {guesses} av {max_guesses} gånger. Försök igen!")
