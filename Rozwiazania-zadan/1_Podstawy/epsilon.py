# Programowanie I R
# Zadanie epsilon

# Wykorzystamy funkcję math.nextafter(x, y), dostępną w Pythonie od wersji 3.9.0.
# Zadanie to można również rozwiązać, korzystając z metody bisekcji.

# math.nextafter(x, y) zwraca liczbę zmiennoprzecinkową następującą
# po x w kierunku y.

import math

print(math.nextafter(1.0, math.inf) - 1.0)

# Równoważnie można napisać np.
#    print(math.nextafter(1.0, 3.0) - 1.0)