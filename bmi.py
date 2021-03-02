# Programowanie I R
# Zadanie bmi

weight = float(input("Podaj masę ciała (w kilogramach): "))
height = float(input("Podaj wzrost (w metrach): "))

bmi = weight/(height**2) 

print("BMI = {0}".format(bmi))

if(bmi < 18.5):
   print("Niedowaga.")

elif(bmi >= 18.5 and bmi < 25):
   print("Waga prawidłowa.")

elif(bmi >= 25 and bmi < 30):
   print("Nadwaga.")

elif(bmi >=30):
   print("Otyłość.")