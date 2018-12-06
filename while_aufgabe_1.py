# Erstellen der Schleife
zahl = 1

while zahl != 0:
    print("Bitte einen beliebigen inch wert eingeben der in cm umgrechnet werden soll")
    inzahl = input()
    zahl = int(inzahl)
    um = 2.54
    fertig = um*zahl
    print(zahl, "inch sind", fertig, "cm")
print("Ende")