# Programowanie I R
# Zadanie fspeed

# Funkcja fspeed()
#    Argumenty:
#       fun - funkcja.
#       *args - krotka.
#          Argumenty pozycyjne wywołania funkcji fun.
#       *kwargs - słownik.
#          Argumenty kluczowe wywołania funkcji fun.
#    Wynik:
#       Wartość dowolnego typu.
#          Wynik wywołania fun(*args, **kwargs).
#       Liczba całkowita.
#          Czas wykonania wywołania fun(*args, **kwargs).
def fspeed(fun, *args, **kwargs):
    import time
    
    time_start = time.perf_counter_ns()
    result = fun(*args, **kwargs)
    time_stop = time.perf_counter_ns()

    return result, time_stop - time_start

# Funkcje testowe
def fun(a, b, c):
    return a + b + c

def delay(t):
    import time
    time.sleep(t)

def fff(m, h, name="Bartek", age=18):
    return f"{name} ma {age} lat. Jego BMI wynosi {m/h**2:.2f}"

# Główny program
print("print(\"DOM\") *************************************")
result, time = fspeed(print, "DOM")
print(f"Wartość zwrócona przez funkcję: {result}.\nCzas wykonania funkcji: {time} ns.")
print()

print("fun(1, 2, 3) *************************************")
result, time = fspeed(fun, 1, 2, 3)
print(f"Wartość zwrócona przez funkcję: {result}.\nCzas wykonania funkcji: {time} ns.")
print()

print("delay(1) *****************************************")
result, time = fspeed(delay, 1)
print(f"Wartość zwrócona przez funkcję: {result}.\nCzas wykonania funkcji: {time} ns.")
print()

print("fff *************************************")
result, time = fspeed(fff, 70, 1.8)
print(f"Wartość zwrócona przez funkcję: {result}.\nCzas wykonania funkcji: {time} ns.")