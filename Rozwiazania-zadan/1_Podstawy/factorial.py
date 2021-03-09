# Programowanie I R
# Zadanie factorial

# Funkcja ifactorial()
#    Iteracyjne obliczanie silni liczby naturalnej.
#
#    Argumenty:
#       n - liczba naturalna.
#
#    Wynik:
#       Liczba naturalna.
#          Silnia liczby n.
def ifactorial(n):
    if n <= 1: return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Funkcja rfactorial()
#    Rekurencyjne obliczanie silni liczby naturalnej.
#
#    Argumenty:
#       n - liczba naturalna.
#
#    Wynik:
#       Liczba naturalna.
#          Silnia liczby n.
def rfactorial(n):
   if n <= 1:
       return 1
   else:
       return n * rfactorial(n - 1)

# Główny program
import time

n = int(input("Podaj liczbę naturalną: "))

# Obliczenie silni - algorytm iteracyjny
i_start = time.perf_counter_ns()
result_i = ifactorial(n)
i_stop = time.perf_counter_ns()

print(f"Silnia liczby {n} - algorytm iteracyjny:")
print(f"\tWynik: {result_i}.".expandtabs(3))
print(f"\tCzas wykonania: {i_stop - i_start} ns.".expandtabs(3))

# Obliczenie silni - algorytm rekurencyjny
r_start = time.perf_counter_ns()
result_r = rfactorial(n)
r_stop = time.perf_counter_ns()

print(f"Silnia liczby {n} - algorytm rekurencyjny:")
print(f"\tWynik: {result_r}.".expandtabs(3))
print(f"\tCzas wykonania: {r_stop - r_start} ns.".expandtabs(3))