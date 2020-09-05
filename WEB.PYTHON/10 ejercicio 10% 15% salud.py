income = float(input("¿Cual es tu porcentaje? "))
if income < 10000:
    tax = 5
elif income < 200000:
    tax = 10
elif income < 3500000:
    tax = 15
else:
    tax = 45
print("Tu porcentaje es " + str(tax) + "%")