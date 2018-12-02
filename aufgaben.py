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
x = input()
y = int(x)

# Überprüfung
if y == c:
    print("Das Ergebnis ist Richtig")
elif y < 0 or y > 100:
    print("Das Ergebnis ist ganz Falsch")
    print("Das Ergebnis:", c)
elif c-1 <= y <= c+1:
    print("Das war fast richtig")
    print("Das Ergebnis ist:", c)
else:
    print("Ihre Eingabe ist leider Falsch")
    print("Das Ergebnis ist:", c)
    

