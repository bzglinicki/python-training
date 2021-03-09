# Programowanie I R
# Zadanie fib

# Analiza różnych algorytmów obliczania wyrazów ciągu Fibonacciego
# dostępna jest na stronie
#    https://www.ics.uci.edu/~eppstein/161/960109.html

# Najprostsza implementacja funkcji fib() ma postać:
#    def fib(n):
#       if n < 1: return 0
#       elif n == 1 or n == 2: return 1
#       else: return fib(n-1) + fib(n-2)
# Taka implementacja jest jednak wysoce nieoptymalna. Łatwo zauważyć,
# że te same obliczenia będą wykonywane wielokrotnie.

# Funkcja fib()
#    Argumenty:
#       n - liczba naturalna.
#    Wynik:
#       Liczba naturalna.
#       n-ty wyraz ciągu Fibonacciego.
#    Wykorzystano algorytm nr 3 ze strony
#       https://www.ics.uci.edu/~eppstein/161/960109.html
def fib(n):
    if n < 1: return 0
    
    a = 1
    b = 1

    if n == 1 or n == 2: return a

    for i in range(3, n + 1):
        c = a + b
        a = b
        b = c

    return b

# Główny program
n = int(input("Podaj liczbę naturalną: "))
print(f"F_{n} = {fib(n)}")