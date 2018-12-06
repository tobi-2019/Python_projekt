# Erstellen der Schleife
fehler = 1
um = 2.54

while fehler == 1:
    print("Bitte einen beliebigen inch wert eingeben der in cm umgrechnet werden soll")
    inzahl = input()
    try:
        zahl = int(inzahl)
        fertig = um*zahl
        print(zahl, "inch sind", fertig, "cm")
        fehler = 0
    except:
        print("Geben sie bitte eine ganze Zahl ein")

print("Ende")