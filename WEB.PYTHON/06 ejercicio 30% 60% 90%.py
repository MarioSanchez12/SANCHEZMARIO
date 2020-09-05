income = float(input("¿Cual es tu porcentaje? "))
if income < 10000:
    tax = 5
elif income < 200000:
    tax = 30
elif income < 3500000:
    tax = 60
elif income < 60000000:
    tax = 90
else:
    tax = 45
print("Tu porcentaje es " + str(tax) + "%")