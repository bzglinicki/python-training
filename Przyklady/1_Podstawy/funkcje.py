# Programowanie I R
# Funkcje

# Materiały:
#    https://realpython.com/defining-your-own-python-function/

# *************************************************************
# Definiowanie i wywoływanie funkcji
# *************************************************************
def f():
    msg = "Funkcja f()"
    print(msg)

print("---> Główny program...")
f()
print("---> Główny program...")
print()

# Funkcja pusta
def stub():
    pass

print("---> Główny program...")
stub()
print("---> Główny program...")
print()

# *************************************************************
# Przekazywanie argumentów
# *************************************************************

def printPersonalData(name, surname, age):
    print(f"Imię i nazwisko: {name} {surname}")
    print(f"Wiek:            {age}")

# Argumenty pozycyjne *****************************************

print("Argumenty pozycyjne:\n")

printPersonalData("Jan", "Nowak", 25)
print()

printPersonalData(25, "Jan", "Nowak")
print()

# Błąd:
#    printPersonalData("Jan", "Nowak")
#    printPersonalData("Jan", "Nowak", 25, "jan.nowak@example.com")

# Argumenty z kluczem *****************************************
print("Argumenty z kluczem:\n")

printPersonalData(name = "Jan", surname = "Nowak", age = 25)
print()

printPersonalData(age = 25, name = "Jan", surname = "Nowak")
print()

# Błąd:
#    printPersonalData(name = "Jan", surname = "Nowak", years = 25)
#    printPersonalData(name = "Jan", surname = "Nowak")
#    printPersonalData(name = "Jan", surname = "Nowak", age = 25, email = "jan.nowak@example.com")

# Mieszanie obu typów argumentów *******************************

print("Argumenty mieszane:\n")

printPersonalData("Jan", surname = "Nowak", age = 25)
print()

printPersonalData("Jan", "Nowak", age = 25)
print()

# Błąd:
#    printPersonalData(name = "Jan", surname = "Nowak", 25)
#    printPersonalData(name = "Jan", "Nowak", age = 25)
#    printPersonalData("Jan", surname = "Nowak", 25)

# Argumenty domyślne *****************************************

def printPersonalDataDef(name = "Bartłomiej", surname = "Kowalski", age = 20):
    print(f"Imię i nazwisko: {name} {surname}")
    print(f"Wiek:            {age}")

print("Argumenty domyślne:\n")

printPersonalDataDef("Jan", "Nowak", 25)
print()

printPersonalDataDef("Jan", "Nowak")
print()

printPersonalDataDef("Jan")
print()

printPersonalDataDef(age = 30)
print()

printPersonalDataDef()
print()

# Przekazywanie przez wartość
print("Przekazywanie przez wartość:")

def inc(x):
    x += 1

k = 5
inc(k)
print(k)
