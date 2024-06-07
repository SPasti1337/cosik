# TC7.py

# Lista temperatur dla jednego tygodnia
temperatures = [21, 19, 22, 25, 28, 23, 22]

# Obliczanie sumy temperatur
sum_temperatures = 0
for temp in temperatures:
    sum_temperatures += temp

# Obliczanie średniej temperatury
average_temperature = sum_temperatures / len(temperatures)

# Wyświetlenie wyniku
print("Średnia temperatura powietrza w ciągu tygodnia wynosi:", average_temperature)
