#zad1
print("\nZad1")
punkty = int(input("Podaj liczbę zdobytych punktów: "))
if punkty > 80:
    print("Zdałeś egzamin")
elif punkty >= 50:
    print("Zdałeś, możesz poprawić wynik egzaminu")
elif punkty < 50:
    print("Nie zdałeś egzaminu, musisz go poprawic")

#zad2
print("\nZad2")
x = int(input("Wprowadź x: "))
y = int(input("Wprowadź y: "))
z = int(input("Wprowadź z: "))

if x > y:
    x, y = y, x
if x > z:
    x, z = z, x
if y > z:
    y,z = z, y

print(f"Uporzadkowane liczby: {x}, {y}, {z}")

#zad3
print("\nZad3")
nazwa_pliku = "raport.xlsx"
if nazwa_pliku.endswith(".xlsx"):
    print("Tak")
else:   print("Nie")

#zad5
print("\nZad5")
print("\na)")

plik = open('notowania_giełdowe.txt', 'r')
print(plik.read())

print("\nb)")

with open("notowania_giełdowe.txt", 'a') as plik:
    plik.write("\nALR, 113")
with open("notowania_giełdowe.txt", "r") as plik:
    print(plik.read())

#zad6
print("\nZad6")
litera = input("Wprowadź literę: ")
if litera.islower():
    print(f"Litera {litera} jest mała")
elif litera.isupper():
    print(f"Litera {litera} jest duża")
else:
    print(f"ERROR: nie wprowadzono litery")

#zad7
print("\nZad7")

haslo = 'pk47!jy0893'

if len(haslo) == 11 and "!" in haslo:
    print(f"Hasło jest poprawne")
else:
    print("Hasło jest niepoprawne")

#zad8
print("\nZad8")

text = "Studiuje-Informatykę"
pierwsze3 = text[0:3]
ostatnie2 = text[-2:]

print(f"Cały tekst: {text}")
print(f"Pierwsze 3 znaki: {pierwsze3}")
print(f"Ostatnie 2 znaki: {ostatnie2}")

#wykonał Konrad Greszta , 75040 - numer albumu.
