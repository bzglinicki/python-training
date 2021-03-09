# Programowanie I R
# Zadanie mostFrequent

# Funkcja mostFrequent()
#    Znajdowanie najczęściej występującego elementu listy.
#
#    Argumenty:
#       lst - lista.
#
#    Wynik:
#       Zmienna dowolnego typu.
#          Najczęściej występujący element listy lst.
def mostFrequent(lst):
	k = lst[0]   # Dotychczas najczęściej występujący element
	freq = 0     # Częstotliwość występowania elementu k

	for i in lst:
		curr_freq = lst.count(i)       # Częstotliwość występowania elementu i
		if(curr_freq > freq):
			freq = curr_freq
			k = i

	return k

# Główny program
input_str = input("Podaj listę liczb całkowitych:\n")
input_lst = input_str.split()

# Konwersja elementów listy z łańcuchów tekstowych na liczby całkowite
for i in range(len(input_lst)):
    input_lst[i] = int(input_lst[i])

print(f"Najczęściej występujący element listy: {mostFrequent(input_lst)}.")