# Programowanie I R
# Zadanie lcollatz

# Wykorzystano algorytm ze strony
#    https://radiusofcircle.blogspot.com/2016/04/problem-14-project-euler-solution-with-python.html

# Definiujemy słownik przechowujący długości nietrywialnej części ciągu dla różnych k.
# Ma on milion elementów, wszystkie mają początkowo wartość 0.
# d[k] będzie długością ciągu Collatza zaczynającego się od k.
d = {n: 0 for n in range(1,1000000)}
d[1] = 1   # Zmieniamy wartość pierwszego elementu
d[2] = 2   # na 1, zaś drugiego elementu - na 2. 

# Pętla przebiega po możliwych wartościach pierwszego wyrazu ciągu.
for n in range(3, 1000000, 1):
    k = n       # Pierwszy wraz ciągu.
    seqlen = 0  # Szukana długość nietrywialnej części ciągu zaczynającego się od k.

    # Obliczamy kolejne wyrazy ciągu, dopóki są one większe od 1.
    while n > 1:
        # Jeśli od pewnego miejsca ciąg pokrywa się z ciągiem, którego długość już
        # obliczyliśmy, korzystamy z otrzymanego wcześniej wyniku.
        if n < k:
            d[k] = d[n] + seqlen
            break   # Przerywamy pętlę while, by przejść do kolejnego ciągu
                    # (o k większym o 1).
        
        # Obliczamy kolejne wyrazy ciągu, korzystając z jego definicji.
        if n%2 == 0:
            n = n/2
            seqlen += 1 # Przechodząc do kolejnego wyrazu, zwiększamy licznik długości ciągu.
        else:
            n = 3*n+1
            seqlen += 1 # Przechodząc do kolejnego wyrazu, zwiększamy licznik długości ciągu.

# Pierwszy wyraz ciągu Collatza o najdłuższej części nietrywialnej.
res_k = list(d.values()).index(max(d.values())) + 1

# Długość ciągu Collatza o najdłuższej części nietrywialnej.
res_len = max(d.values())

print(f"Pierwszy wyraz: {res_k}.")
print(f"Długość części nietrywialnej: {res_len}.")