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
    print("Das Ergebniss ist Richtig")
else:
    print("Ihre Eingabe ist leider Falsch")
    print("Das Ergebniss ist:", c)
    

