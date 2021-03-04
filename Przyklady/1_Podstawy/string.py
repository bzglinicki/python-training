# Programowanie I R
# Łańcuchy tekstowe

# Dokumentacja:
# https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str
# https://docs.python.org/3/library/string.html

# Określanie łańcuchów
'Amicus Plato, sed magis amica veritas'
"Amicus Plato, sed magis amica veritas"

# Stosowanie znaków ' i " wewnątrz łańcuchów
'Amicus "Plato", sed magis amica "veritas"'
"Amicus 'Plato', sed magis amica 'veritas'"
"Amicus \"Plato\", sed magis amica \"veritas\""

# Stosowanie znaku \ wewnątrz łańcuchów
"C:\\Users\\Bartek"
r"C:\Users\Bartek"

# Łańcuchy wieloliniowe
'''
Pierwsza linia.
Druga linia.
Trzecia linia.
'''

"""
Pierwsza linia.
Druga linia.
Trzecia linia.
"""

# ...bez znaku nowego wiersza na początku i na końcu
"""Pierwsza linia.
Druga linia.
Trzecia linia."""

# ...bez znaku nowego wiersza na początku
"""\
Pierwsza linia.
Druga linia.
Trzecia linia.
"""

####################################################################################

# Formatowanie łańcuchów
# Omówienie:
# https://realpython.com/python-formatted-output/

name = "Bartek"
age = 18

# Formatowanie - sposób I (przestarzały) #################################
# Dokumentacja:
# https://docs.python.org/3/library/stdtypes.html#printf-style-string-formatting

"Mam na imię %s." % name
"%s ma %s lat." % (name, age)

"%d %s kosztuje %.2f zł" % (5, "jabłek", 3)

# Formatowanie - sposób II ###############################################
# Dokumentacja:
# https://docs.python.org/3/library/string.html#formatstrings

"{} ma {} lat.".format(name, age)
"{0} ma {1} lat.".format(name, age)
"{1} ma {0} lat.".format(age, name)
"{0} ma {1} lat. {0} jest więc młodym człowiekiem.".format(name, age)

"{0} {1} kosztuje {2:.2f} zł.".format(5, "jabłek", 3)
"{quantity} {item} kosztuje {price:.2f} zł.".format(
            quantity = 5,
            item = "jabłek",
            price = 3
        )

"{0} {x} {1}.".format("Ala", "kota", x = "ma")
# "{0} {x} {2}.".format("Ala", x = "ma", "kota") - BŁĄD!

# Formatowanie - sposób III (zalecany) ###################################
# Dokumentacja:
# https://docs.python.org/3/reference/lexical_analysis.html#f-strings
f"{name} ma {age} lat."
F"{name} ma {age} lat."

# Można stosować dowolne wyrażenia, w tym wywołania funkcji
f"{2 * 3}"
f"{name.upper()} ma {age} lat."

# Możliwe jest również formatowanie łańcuchów wieloliniowych
f"""To jest {name.upper()}.
{name} ma {age} lat.
12 * 9 = {12 * 9}"""

# Nawiasy klamrowe
f"{{70 + 4}}"
f"{{{70 + 4}}}"
f"{{{{70 + 4}}}}"