# Programowanie I R
# Zadanie bmi

m = float(input("Podaj masę ciała (w kilogramach): "))
h = float(input("Podaj wzrost (w metrach): "))
print() # Pusta linia dla estetyki

bmi = m / (h**2)

print(f"BMI = {bmi:.2f}")

if bmi < 18.5:
   print("Niedowaga.")
elif bmi >= 18.5 and bmi < 25:
   print("Waga prawidłowa.")
elif bmi >= 25 and bmi < 30:
   print("Nadwaga.")
else:
   print("Otyłość.")