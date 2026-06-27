# En este taller, practicarás el trabajo con números y operaciones matemáticas para crear una calculadora de división de cuentas. Esta herramienta calculará cuánto debe pagar cada persona después de sumar el costo de la comida y la propina.

running_total = 0
num_of_friends = 4

appetizers = 37.89
main_courses = 57.34
desserts = 39.39
drinks = 64.21

running_total += appetizers + main_courses + desserts + drinks
print("Total bill so far:", round(running_total, 2))


tip_percentage = 0.25

tip = running_total * tip_percentage
print("Tip amount:", round(tip, 2))

running_total += tip
print("Total with tip:", round(running_total, 2))

final_bill = running_total / num_of_friends
each_pays = round(final_bill, 2)
print("Each person pays:", each_pays)