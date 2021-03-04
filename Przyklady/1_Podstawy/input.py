# Programowanie I R
# Funkcja input()

# Dokumentacja:
# https://docs.python.org/3/library/functions.html#input

print("Jak masz na imię?")
name = input()
print("Witaj, " + name + "!")

name = input("Jak masz na imię? ")
print("Witaj, " + name + "!")

name = input("Jak masz na imię?\n")
print("Witaj, " + name + "!")

# Funkcja input() zwraca zawsze łańcuch tekstowy
number = input("Podaj jakąś liczbę: ")
print(type(number))

# W celu otrzymania wartości innych typów musimy dokonać konwersji
number = float(input("Podaj jakąś liczbę: "))
print(type(number))
print(50 + number) # Bez konwersji, czyli użycia float(...), tu byłby błąd

# Możemy pobrać kilka wartości jednocześnie
name, age, place = input("Podaj swoje imię, wiek i miejsce zamieszkania, oddzieając je spacjami:\n").split()
print("Twoje dane: " + name, age, place, sep=", ")