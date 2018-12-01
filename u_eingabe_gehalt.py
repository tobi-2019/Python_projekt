# Ausgabe
print("Geben sie bitte ihr monatliches brutto Gehalt in Euro ein")
a = input()
b = int(a)
print("Geben sie ihren Familien stand ein")
print("ledig = 1")
print("Verheiratet = 2")
f = input()
fam = int(f)

# Daten Sammlung und Umrechnug
m = 0.18
n = 0.22
k = 0.26
ö = 1
ä = 2
p = int(ö)
ü = int(ä)
x = float(m)
y = float(n)
c = float(k)
q = b*x
w = b*y
e = b*c
u = float(q)
i = float(w)
o = float(e)

""" Rechnug
if b < 2500:
    print("Sie Zahlen 18% Steuern, es ergibt sich eine Steuer von", u, "Euro")
elif b < 4000 and :
    print("Sie Zahlen 22% Steuern, es ergibt sich eine Steuer von", i, "Euro")
else:
    print("Sie Zahlen 26% Steuern, es ergibt sich eine Steuer von", o, "Euro")"""

# Anzeige
if fam == p and b > 4000:
    print("Sie Zahlen 26% Steuern, es ergibt sich eine Steuer von", o, "Euro")
elif fam == ü and b > 4000:
    print("Sie Zahlen 22% Steuern, es ergibt sich eine Steuer von", i, "Euro")
elif fam == p and b < 4000:
    print("Sie Zahlen 22% Steuern, es ergibt sich eine Steuer von", i, "Euro")
elif fam == ü and b < 4000:
    print("Sie Zahlen 22% Steuern, es ergibt sich eine Steuer von", u, "Euro")
else:
    print("Es ist ein Fehler augetreten")
