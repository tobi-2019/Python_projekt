# Importieren von Modulen
import random

# Modul config
random.seed

# Erstellen der Variablen
a = random.randint(1,10)
b = random.randint(1,10)
c = a + b

# Anzeige
print("Die Aufgabe:", a, "+", b, "=", "?")

# Input
for i in 1,2,3,4:
    x = input()
    y = int(x)
    if y == c:
        print("Ihre eingabe ist Richtig")
        print("Sie haben", i, "versuche gebraucht")
        break
    elif y-1 < c < y+1:
        print("Ihre eingabe ist fast Richtig")
        print("Sie haben noch", 4-i, "versuche")
    else:
        print("Ihre einagbe ist Falsch")
        print("Sie haben noch", 4-i, "versuche")
print("Ende")

