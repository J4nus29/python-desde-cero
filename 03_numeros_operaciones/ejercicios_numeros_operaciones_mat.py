# ====================================
# EJERCICIO 1 - ENTEROS Y FLOATS
# ====================================

# Ejercicio 1.1

edad = 27
peso = 83.0
altura = 1.78
print(edad, peso, altura)

# Ejercicio 1.2

print(type(edad))
print(type(peso))
print(type(altura))

# Ejercicio 1.3

salario = 3200000
bono = 500000

print("Salario total:", salario + bono)

# Ejercicio 1.4

precio = 5800000
abono = 1700000

print("Saldo pendiente:", precio - abono)

# Ejercicio 1.5

lagartijas = 40
series = 5

print("Total lagartijas:", lagartijas * series)

# Ejercicio 1.6

distancia = 180
horas = 3

velocidad_promedio = distancia / horas 
print("Velocidad promedio:", velocidad_promedio)

# ====================================
# EJERCICIO 2 - OPERACIONES BASICAS
# ====================================

# Ejercicio 2.1 - Salario mensual

primera_quincena = 1550000
segunda_quincena = 1720000

salario_total_mes = primera_quincena + segunda_quincena
print("El salario total del mes es:", salario_total_mes)

# Ejercicio 2.2 - Ahorro para un viaje

ahorro = 2300000
ahorro_mensual = 450000

ahorro_total = ahorro + ahorro_mensual
print("Ahorro total fin de mes:", ahorro_total)

# Ejercicio 2.3 - Peso ideal

peso_actual = 83
meta_peso = 78

peso_deseado = peso_actual - meta_peso
print("El total de kilos a bajar para el peso ideal es de:", peso_deseado)

# Ejercicio 2.4 - Entrenamiento

lagartijas = 60
dias_consecutivos = 7

total_lagartijas_semanales = lagartijas * dias_consecutivos
print("La cantidad de lagartijas realizadas en la semana fue de:", total_lagartijas_semanales)

# Ejercicio 2.5 - Consumo de combustible

distancia = 420
consumo_combustible = 35

total_consumo_combustible = distancia / consumo_combustible
print("El consumo de combustible en kilometros por litro fue de:", total_consumo_combustible)

# ====================================
# EJERCICIO 3 - MODULO, DIVISION ENTERA Y POTENCIA
# ====================================

# Ejercicio 3.1 - Salones de clase

num_estudiantes = 53
estudiantes_por_salon = 8

print("Los salones llenos son:", num_estudiantes // estudiantes_por_salon)
print("Estudiantes que se quedan sin salon son:", num_estudiantes % estudiantes_por_salon)

# Ejercicio 3.2 - Conos de entrenamiento

conos_instructor = 97
grupos = 12

print("La cantidad de conos que recibe cada grupo es de:", conos_instructor // grupos)
print("La cantidad de conos sobrantes es de:", conos_instructor % grupos)

# Ejercicio 3.3 - Potencia

num_uno = 2
num_dos = 10

potencia = num_uno ** num_dos

print("La potencia de 2 elevado a la 10 es de:", potencia)

# Ejercicio 3.4 - Area de un cuadrado

cuadrado = 15
area = cuadrado ** 2
area_cuadrado = area
print("El area del cuadrado es de:", area_cuadrado )

# ====================================
# EJERCICIO 4 - CONVERSIONES Y FUNCIONES NUMERICAS
# ====================================

# ------------------------------------
# int()
# Convierte un número decimal a entero
# Elimina la parte decimal (NO redondea)
# ------------------------------------

numero_decimal = 27.99
numero_entero = int(numero_decimal)

print("Número original:", numero_decimal)
print("Convertido a entero:", numero_entero)


# ------------------------------------
# float()
# Convierte un entero en un número decimal
# ------------------------------------

edad = 27
edad_decimal = float(edad)

print("Edad original:", edad)
print("Edad convertida a float:", edad_decimal)


# ------------------------------------
# round()
# Redondea un número al entero más cercano
# ------------------------------------

promedio = 8.7

print("Número original:", promedio)
print("Número redondeado:", round(promedio))


# ------------------------------------
# round() con decimales
# Conserva la cantidad de decimales indicada
# ------------------------------------

pi = 3.14159265

print("Pi original:", pi)
print("Pi con 2 decimales:", round(pi, 2))
print("Pi con 4 decimales:", round(pi, 4))


# ------------------------------------
# abs()
# Devuelve el valor absoluto
# Convierte un número negativo en positivo
# ------------------------------------

temperatura = -15

print("Temperatura:", temperatura)
print("Valor absoluto:", abs(temperatura))


# ------------------------------------
# pow()
# Eleva un número a una potencia
# Hace lo mismo que **
# ------------------------------------

base = 2
exponente = 10

print("Potencia:", pow(base, exponente))


# ------------------------------------
# Comparación entre pow() y **
# Ambos producen el mismo resultado
# ------------------------------------

print("Con ** :", 2 ** 10)
print("Con pow():", pow(2, 10))


# ------------------------------------
# Diferencia entre int() y round()
# ------------------------------------

numero = 8.9

print("Número original:", numero)
print("int() elimina el decimal:", int(numero))
print("round() redondea:", round(numero)) 

# ====================================
# EJERCICIO 5 - ASIGNACIÓN AUMENTADA
# ====================================

# Ejercicio 5.1 - Ahorro Mensual

ahorro = 2500000
ahorro_mensual = 450000

ahorro += ahorro_mensual

print("El ahorro total mensual de este mes es de:",  ahorro)

# ===================================== 

ahorro = 2500000
ahorro += 450000

print("El ahorro total mensual de este mes es de:", ahorro)

# Ejercicio 5.2 - Pago de una deuda

deuda_total = 3800000
abono_deuda = 750000

deuda_total -= abono_deuda

print("El saldo restante luego del abono es de:", deuda_total)

# =======================================

deuda_total = 3800000
deuda_total -= 750000

print("El saldo restante luego del abono es de:", deuda_total)

# Ejercicio 5.3 Entrenamiento

lagartijas = 35
series = 6

lagartijas *= series

print("El total de lagartijas realizadas fue de:", lagartijas)

# =======================================

lagartijas = 35
lagartijas *= 6

print("El total de lagartijas realizadas fue de:", lagartijas)

# Ejercicio 5.4 - Velodidad promedio

distancia = 240
tiempo = 4

distancia /= tiempo 

print("La distancia promedio en 4 horas fue de:", distancia)
print(type(distancia))

# ======================================

distancia = 240
distancia /= 4

print("La distancia promedio en 4 horas fue de:", distancia)

# Ejercicio 5.5 - Division entera

estudiantes = 98
grupos_de = 9

estudiantes //= grupos_de

print("La cantidad de grupos completos es de:", estudiantes)

# =====================================

estudiantes = 98
estudiantes //= 9

print("La cantidad de grupos completos es de:", estudiantes)

# Ejercicio 5.6 - Módulo

estudiantes = 98
grupos_de = 9

estudiantes %= grupos_de

print("La cantidad de estudiantes que sobran luego de formar grupos de 9 es de:", estudiantes)

# ======================================

estudiantes = 98
estudiantes %= 9

print("La cantidad de estudiantes que sobran luego de formar grupos de 9 es de:", estudiantes)

# Ejercicio 5.7 - Potencia

num_uno = 2
num_dos = 8

num_uno **= num_dos

print("El numero 2 elevado a la potencia 8 es de:", num_uno)

# =======================================

num_uno = 2
num_uno **= 8

print("El numero 2 elevado a la potencia 8 es de:", num_uno)

# Ejercicio 5.8 - Cadena de texto

nombre = "Juan"
nombre += " Esteban Muñoz Vasquez"

print("El nombre completo es:", nombre)