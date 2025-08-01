
# ? LAB Variables: Un converidor simple

# Salida Esperada:
# 7.38 millas son 11.88 kilómetros
# 12.25 kilómetros son 7.61 millas

kilometers = 12.25
miles = 7.38

miles_to_kilometers = miles * 1.61
kilometers_to_miles = kilometers / 1.61

print(miles, "millas son", round(miles_to_kilometers, 2), "kilómetros")
print(kilometers, "kilómetros son", round(kilometers_to_miles, 2), "millas")

# Convertidor de Dolares a Quetzales

USD = 20
GTQ = 150

USDtoGTQ = USD * 7.72
GTQtoUSD = GTQ / 7.72

print(USD, "Dolares son: ", round(USDtoGTQ, 2), "Quetzales")
print(GTQ, "Quetzales son: ", round(GTQtoUSD, 2), "Dolares")