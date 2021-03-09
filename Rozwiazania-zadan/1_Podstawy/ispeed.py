# Programowanie I R
# Zadanie ispeed

# Funkcja mean()
#    Argumenty:
#       nums - lista liczb całkowitych.
#    Wynik:
#       Liczba całkowita
#          Średnia arytmetyczna liczb z listy nums
def mean(nums):
    return float(sum(nums)) / max(len(nums), 1)

# Funkcja ispeed()
#    Argumenty:
#       fun - funkcja.
#       args - lista liczb całkowitych.
#          Kolejne argumenty wywołania funkcji fun.
#    Wynik:
#       Wartość dowolnego typu.
#          Wynik wywołania fun(*args, **kwargs).
#       Liczba całkowita.
#          Czas wykonania wywołania fun(*args, **kwargs).
def fspeed(fun, *args):
    import time
    
    results = []
    times = []

    for x in args:
        result_x = 0
        times_x = []
        for i in range(5):
           time_start = time.perf_counter_ns()
           result = fun(x)
           time_stop = time.perf_counter_ns()

           result_x = result
           times_x.append(time_stop - time_start)
        
        results.append(result_x)
        times.append(mean(times_x))
        
    return results, times

# Funkcje testowe
def f1(n):
    return n

def f2(n):
    return n**2

def f3(n):
    import math
    return math.sqrt(n)

# Główny program
print("f1(n) ****************************************")
results, times = fspeed(f1, 1, 2, 3)
print(f"Wartości zwrócone przez funkcję: {results}.\nCzasy wykonania funkcji (ns): {times}.")
print()

print("f2(n) ****************************************")
results, times = fspeed(f2, 1, 2, 3)
print(f"Wartości zwrócone przez funkcję: {results}.\nCzasy wykonania funkcji (ns): {times}.")
print()

print("f3(n) ****************************************")
results, times = fspeed(f3, 1, 2, 3)
print(f"Wartości zwrócone przez funkcję: {results}.\nCzasy wykonania funkcji (ns): {times}.")