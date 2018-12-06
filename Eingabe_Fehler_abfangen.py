fehler = 1

while fehler == 1:
    print("geben sie eine ganze Zahl ein")
    z = input()
    try:
        zahl = int(z)
        print("Sie haben eine Zahl richtig eingegeben")
        fehler = 0
    except:
        print("Sie haben keine ganze Zahl eingegeben")
    

print("Ende des Pogramms")