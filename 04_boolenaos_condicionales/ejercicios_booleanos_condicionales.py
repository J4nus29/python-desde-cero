# ====================================
# EJERCICIO 6 - BOOLEANOS Y CONDICIONALES
# ====================================

# Ejercicio 6.1 - Mayor de edad

edad = 27

if edad >= 18:
    print("Es mayor de edad")


# Ejercicio 6.2 - Acceso al sistema

es_admin = False

if es_admin:
    print("Bienvenido administrador")
else:
    print("Acceso denegado")


# Ejercicio 6.3 - Descuento para estudiantes

edad = 27
es_estudiante = False

if edad < 18 or es_estudiante:
    print ("Tiene derecho a descuento")
else:
    print("No tiene descuento")


# Ejercicio 6.4 - Derecho al voto

edad = 25
es_ciudadano = True

if edad >= 18 and es_ciudadano:
    print("El ciudadano tiene derecho al voto")
else:
    print("El ciudadano no tiene derecho a votar, no cumple con los requisitos necesarios")


# Ejercicio 6.5 - Acceso al panel

es_bloqueado = False

if not es_bloqueado:
    print("Acceso permitido")
else:
    print("Cuenta bloqueada")

# Ejercicio 6.6 - RETO

edad = 20
es_estudiante = True
es_ciudadano = False

if edad >= 18 and (es_estudiante or es_ciudadano):
    print("Puede acceder al beneficio especial")
else:
    print("No tiene derecho al beneficio especial")
