# Programowanie I R
# Zadanie lineq

# "NAPIS".expandtabs(n) ustala długośćś tabulatorów
# (znaków '\t') w łańcuchu "NAPIS" na n

print("ax + b = 0")
a = float(input("\ta = ".expandtabs(3)))
b = float(input("\tb = ".expandtabs(3)))
print()

x = -b / a

print("Rozwiązanie:\n\tx =".expandtabs(3), x)