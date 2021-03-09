# Programowanie I R
# Zadanie nextPrime

# Funkcja isPrime()
#    Argumenty:
#       n - liczba naturalna.
#    Wynik:
#       Wartość logiczna.
#       True, jeśli n jest liczbą pierwszą,
#       False w przeciwnym przypadku.
#    Wykorzystano prosty algorytm opisany na Wikipedii:
#       https://en.wikipedia.org/wiki/Primality_test#Simple_methods
def isPrime(n):
    if n <= 1: return False   # Te dwie instrukcje można zapisać łącznie:
    if n <= 3: return True    #   if n <= 3: return n > 1
    if n % 2 == 0 or n % 3 == 0: return False

    i = 5
    while i ** 2 <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Funkcja nextPrime()
#    Argumenty:
#       n - liczba naturalna.
#    Wynik:
#       Liczba naturalna.
#       Najmniejsza liczba pierwsza większa od n.
def nextPrime(n):
    if (n <= 1): return 2

    k = n
    prime = False

    while not prime:
        k += 1
        prime = isPrime(k)

    return k
  
# Główny program
n = int(input("Podaj liczbę naturalną: "))
print(f"Najmniejsza liczba pierwsza większa od {n} to {nextPrime(n)}.")