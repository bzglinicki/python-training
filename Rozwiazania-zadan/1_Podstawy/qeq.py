# Programowanie I R
# Zadanie qeq

# math - funkcje matematyczne
import math

# cmath - funkcje matematyczne liczb zespolonych
import cmath

print("ax^2 + bx + c = 0")
a = float(input("\ta = ".expandtabs(3)))
b = float(input("\tb = ".expandtabs(3)))
c = float(input("\tc = ".expandtabs(3)))
print()

delta = (b**2) - (4*a*c)

if delta == 0:
    x0 = -b / (2*a)
    print("Rozwiązanie:\n\tx0 = {:.2f}".format(x0).expandtabs(3))
elif delta > 0:
    x1 = (-b - math.sqrt(delta)) / (2*a)
    x2 = (-b + math.sqrt(delta)) / (2*a)
    print("Rozwiązania:\n\tx1 = {0:.2f}\n\tx2 = {1:.2f}".format(x1, x2).expandtabs(3))
else:
    x1 = (-b - cmath.sqrt(delta)) / (2*a)
    x2 = (-b + cmath.sqrt(delta)) / (2*a)
    print(f"Rozwiązania:\n\tx1 = {x1:.2f}\n\tx2 = {x2:.2f}".expandtabs(3))