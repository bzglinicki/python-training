# Programowanie I R
# Funkcje

# Materiały:
#    https://www.w3schools.com/python/python_functions.asp
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

# Wartości domyślne ******************************************

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

# Argumenty są przekazywane "przez wartość"!
print("Przekazywanie przez wartość:")

def inc(x):
    x += 1   # x = x + 1

k = 5
inc(k)
print(k)

# *************************************************************
# Instrukcja return. Zwracanie wartości
# *************************************************************

def g():
    print("Funkcja g() po raz pierwszy.")
    return
    print("Funkcja g() po raz drugi.")   # To się nie wykona!

print("---> Główny program...")
g()
print("---> Główny program...")
print()

# Instrukcję return można wykorzystać np. do reagowania na niepoprawne
# wartości argumentów
def h(x):
    if x < 0:     # Argument niepoprawny, nie rób nic.
        return

    if x > 100:   # Argument niepoprawny, nie rób nic.
        return

    print(x)

h(-3)
h(105)
h(64)

# Zwracanie wartości
def message():
    return "Pozdrawiam!"

msg = message()
print(msg)