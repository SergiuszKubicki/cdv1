'''
print("1111")
print(8)

#potęgowanie
pow = 2 ** 10
print(pow)

text = "CDV"
print(text * 2)

#pobieranie danych z klawiatury
# + konkatenacja = polaczenie 2 stringow

name = input()
print("Twoje imie :" + name)

surname=input()
print("Twoje imie: " + name + ", nazwisko: "+ surname)

length = len(surname)
print(length)
print(type(surname))
print(type(length))

lenght = str(length)
print(type(length))
'''

#użytkownik podaje z klawiatury swoje dane
#imie nazwisko wiek
#wystwietl dane w formacseie:
#imie i nazwisko: ..., wiek:... lat

name = input()
surname = input()

print("twoje imie: " + name + ",nazwisko: " + surname + "")

print("\nPodaj swój wiek:", end="")
surname="Kowalski"
firstLetter = surname[0]

lastLetter = surname[len(surname) -1]
print(lastLetter)

#konwersja
x = "5"
print(type(x))
x = int(x)
print(type(x))

y = 4
print(type(y)) #int
y = y / 2
print(type(y)) #float
print(y) #2.0


surname = "Kowalski"
print()
print(surname[0]) #k
print(surname[0:3])#kow
print(surname[-2])#k    
print(surname[-2:])#ki
print(surname[:-2])#kowalsk
print(surname[:-2:2])#kwl
