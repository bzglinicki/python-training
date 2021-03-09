# Programowanie I R
# Zadanie speed

# Porównanie zegarów w Pythonie:
# https://www.webucator.com/blog/2015/08/python-clocks-explained/

import time

a = float(input("Podaj pierwszą liczbę: "))
b = float(input("Podaj drugą liczbę: "))
c = 0

# time.perf_counter() ################################################

add_start = time.perf_counter_ns()
c = a + b
add_stop = time.perf_counter_ns()

mul_start = time.perf_counter_ns()
c = a * b
mul_stop = time.perf_counter_ns()

print("perf_counter:")
print("Dodawanie: {0}".format(add_stop - add_start))
print("Mnożenie: {0}".format(mul_stop - mul_start))
print("Różnica: {0}".format((mul_stop - mul_start) - (add_stop - add_start)))
print()

# time.process_time() ################################################

add_start = time.process_time_ns()
c = a + b
add_stop = time.process_time_ns()

mul_start = time.process_time_ns()
c = a * b
mul_stop = time.process_time_ns()

print("process_time:")
print("Dodawanie: {0}".format(add_stop - add_start))
print("Mnożenie: {0}".format(mul_stop - mul_start))
print("Różnica: {0}".format((mul_stop - mul_start) - (add_stop - add_start)))

# Dla krótkich fragmentów kodu można też wykorzystać
# funkcję timeit() z modułu timeit.
# Przykłady: https://www.geeksforgeeks.org/timeit-python-examples/