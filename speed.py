# Programowanie I R
# Zadanie speed

import time

a = float(input("Podaj pierwszą liczbę: "))
b = float(input("Podaj drugą liczbę: "))

add_start = time.perf_counter()
c = a + b
add_stop = time.perf_counter()

mul_start = time.perf_counter()
c = a * b
mul_stop = time.perf_counter()

print("Dodawanie: {0}".format(add_stop - add_start))
print("Mnożenie: {0}".format(mul_stop - mul_start))
print("Różnica: {0}".format((mul_stop - mul_start) - (add_stop - add_start)))