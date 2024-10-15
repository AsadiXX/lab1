#Zad .1
# a)typ wyników określonych działań:

#Typ wyników działania 1+2:
x = 1 + 2
print (type(x))
#<class 'int'>

#Typ wyników działania 1+4.5:
x = 1 + 4.5
print (type (x))
#<class 'float'>

#Typ wyników działania 3 / 2:
x = 3/2
print(type(x))
#<class 'float'>

#Typ wyników działania 4 / 2:
x = 4 / 2
print (type(x))
#<class 'float'>

#Typ wyników działania 3 // 2:
x = 3 // 2
print(type(x))
#<class 'int'>

#Typ wyników działania -3 // 2:
x = -3 // 2
print (type(x))
#<class 'int'>

#Typ wyników działania -3 // 2:
x = -3 // 2
print (type(x))
#<class 'int'>

#Typ wyników działania 11 % 2:
x = 11 % 2
print (type(x))
#<class 'int'>

#Typ wyników działania 2 ** 10: x=2** 10
print(type(x))
#<class 'int'>

#Typ wyników działania 8 ** (1/3):
x = 8 ** (1/3)
print (type(x))
#<class 'float'>

#b) Sprawdź i wyjaśnij działanie następujących instrukcji:
x = int (3.0)
print (type(x))
#<class 'int'>

x = float (3)
print (type (x))
#<class 'float'>

x = float("3")
print (type(x))
#<class 'float'>

x = str(12.4)
print (type (x))
#<class 'str'>

x = bool (0)
print (type (x))
#<class 'bool'>

#Zad. 2
uczelnia = "Studiuję na WSIiZ"
print(uczelnia)
#Studiuję na WSIiZ

#Zad. 3
imie = 'Jan'
wiek = 20
wzrost = 178

print('Nazywam się',imie,'i mam',wiek,'lat.', end="\n")
print('Mój wzrost to',wzrost)
# Nazywam się Jan i mam 20 lat.
# Mój wzrost to 178

#Zad. 4
Cena = 39.99
Rabat = 0.2
po_rabacie = Cena - (Cena*Rabat)
print(round(po_rabacie, 2))
#31.99

#Zad. 5
#Pobranie danych od użytkownika
a = float(input("Podaj długość boku a: "))
b = float(input("Podaj długość boku b: "))

#Obliczenia
pole = a*b
obw = (2*a)+(2*b)

#Wyświetlenie wyniku
print(f"Pole wynosi {pole}", end="\n")
print(f"obwód wynosi {obw}")

#Zad. 6
#Pobranie danych od użytkownika
droga = float(input("Podaj drogę pokonaną w kilometrach przez samochód: "))
srednie_spalanie = float(input("Podaj średnie spalanie w litrach na 100km przez samochód: "))

#Obliczenia
zuzycie = (droga*srednie_spalanie)/100
koszta = zuzycie * 6.5

#Wyświetlenie informacji o zużyciu paliwa i kosztach podróży
print(f"Przewidywane zużycie paliwa wynosi: {round(zuzycie, 2)} l")
print(f"Szacowane koszty podróży: {round(koszta, 2)} zł")

#A)
#Wczytanie losowej liczby z zakresu (0,1000)
import random
droga_los = random.randint(0,1000)

#Pobranie danych od użytkownika
srednie_spalanie = float(input("Podaj średnie spalanie w litrach na 100km przez samochód: "))
cena_paliwa = float(input("Podaj aktualną cenę za litr paliwa: "))

#Obliczenia
zuzycie = (droga_los*srednie_spalanie)/100
koszta = zuzycie * cena_paliwa

#Wyświetlenie informacji o zużyciu paliwa i kosztach podróży
print(f"Przewidywane zużycie paliwa za przejechanie {droga_los} km wynosi: {round(zuzycie, 2)} l")
print(f"Szacowane koszty podróży: {round(koszta, 2)} zł")

#Zad. 9 (dodatkowe)
#Pobranie danych od użytkownika
liczba1 = float(input("Podaj pierwszą liczbę: "))
liczba2 = float(input("Podaj drugą liczbę: "))

#Obliczanie wyników dla wszystkich operacji
dodawanie = liczba1 + liczba2
odejmowanie = liczba1 - liczba2
mnozenie = liczba1 * liczba2
dzielenie = liczba1 / liczba2 if liczba2 != 0 else "Nie można dzielić przez zero"
potegowanie = liczba1 ** liczba2

#Wyświetlanie wyników
print(f"Wyniki działań matematycznych dla liczb {liczba1} i {liczba2}:")
print(f"Dodawanie: {dodawanie}")
print(f"Odejmowanie: {odejmowanie}")
print(f"Mnożenie: {mnozenie}")
print(f"Dzielenie: {dzielenie}")
print(f"Potęgowanie: {potegowanie}")