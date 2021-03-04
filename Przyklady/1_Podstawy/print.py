# Programowanie I R
# Funkcja print()

# Dokumentacja:
# https://docs.python.org/3/library/functions.html#print

# Wartościowe informacje:
# https://realpython.com/python-print/

# Wypisanie pustej linii
print()

# Wypisanie łańcucha znaków
print("Dubito ergo sum.")

message = "Dubito ergo sum."
print(message)

# Wszelkie operacje na łańcuchach są oczywiście dozwolone
name = "Bartek"
print("Cześć, " + name + "!")
print(f"Cześć, {name}!")

age = 18
print(name + " ma " + str(age) + " lat.") # Konieczna konwersja!
print(f"{name} ma {age} lat.")

# Funkcja print() przyjmuje argumenty dowolnego typu, konwersja nie jest konieczna
print("ABC")    # str
print(2)        # int
print(1.3)      # float
print(5 + 7j)   # complex
print(True)     # bool
# etc.

#################################################################################

# Funkcja print() może przyjmować dowolnie wiele argumentów
# Kolejne argumenty są wypisywane jeden po drugim i oddzielane spacją
name = "Bartek"
age = 18
print(name, "ma", age, "lat.")

# Możemy zmienić separator, zastępując spację dowolnym łańcuchem
print("non", "omnis", "moriar")                  # spacja
print("non", "omnis", "moriar", sep=" ")         # spacja
print("non", "omnis", "moriar", sep=None)        # spacja
print("non", "omnis", "moriar", sep="")          # brak
print("non", "omnis", "moriar", sep="\t")        # tabulator
print("non", "omnis", "moriar", sep=", ")        # przecinek i spacja
print("non", "omnis", "moriar", sep=" | ")       # pionowa kreska
print("non", "omnis", "moriar", sep=" <---> ")   # można użyć dowolnego łańcucha
print("non", "omnis", "moriar", sep="\n")        # nowa linia

# Pojawienie się separatora na początku i końcu można wymusić,
# dodając puste łańcuchy
print("non", "omnis", "moriar", sep="|")
print("", "non", "omnis", "moriar", "", sep="|")

#################################################################################

# Funkcja print() pozwala określić ciąg znaków umieszczany na końcu wypisywanego łańcucha
# Domyślnie jest to pojedynczy znak nowej linii
print("non", "omnis", "moriar")             # nowa linia
print("OK")

print("non", "omnis", "moriar", end="\n")       # nowa linia
print("OK")

print("non", "omnis", "moriar", end=None)       # nowa linia
print("OK")

print("non", "omnis", "moriar", end="")         # nowa linia
print("OK")

print("non", "omnis", "moriar", end=". ")       # kropka i spacja
print("OK")

print("non", "omnis", "moriar", end=" ---> ")   # dowolny ciąg znaków
print("OK")

# "end" i "sep" można łączyć
print("Mercurius", "Venus", "Terra", "Mars", sep=', ', end=', ')
print("Iuppiter", "Saturnus", "Uranus", "Neptunus", sep=', ')