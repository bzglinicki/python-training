# Programowanie I R
# Zadanie collatz

# Omówienie i przykłady użycia słowa kluczowego yield:
#    https://www.geeksforgeeks.org/use-yield-keyword-instead-return-keyword-python/
#    https://realpython.com/introduction-to-python-generators/

# Funkcja collatz()
#    Argumenty:
#       n - liczba naturalna
#    Wynik:
#       Lista liczb naturalnych.
#       Początkowe wyrazy ciągu Collatza aż do pierwszego wyrazu o wartości 1 włącznie.
def collatz(n):
    yield n
    while n != 1:
        if n % 2 == 0:
            n = n // 2
            yield n
        else:
            n = 3 * n + 1
            yield n

# Główny program
k = int(input("Podaj liczbę naturalną: "))
print(f"Ciąg Collatza zaczynający się od {k} do pierwszego wystąpienia 1:")
print(f"\t{list(collatz(k))}".expandtabs(3))