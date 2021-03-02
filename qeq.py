# Programowanie I R
# Zadanie qeq

# Liczby zespolone
import cmath

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

delta = (b**2) - (4*a*c)

if delta == 0:
    sol = (-b)/(2*a)
    print("x0 = {0}".format(sol))
else:
    sol1 = (-b - cmath.sqrt(delta))/(2*a)
    sol2 = (-b + cmath.sqrt(delta))/(2*a)
    print("x1 = {0}\nx2 = {1}".format(sol1,sol2))