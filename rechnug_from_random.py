# Importieren des Modules
import random

# Installation des Generators
random.seed()

# Berechnug der Werte
a = random.randint(1,10)
b = random.randint(1,10)
c = a + b
print("Die Aufgabe Lautet", a, "+", b)

# Eingabe
print("Bitte eine Zahl eingeben")
z = input()
zf = int(z)

# Ausgabe
print("Ihre Eingabe:", zf)
print("Das Ergebnis:", c)