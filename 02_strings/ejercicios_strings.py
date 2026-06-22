# ===================================
# Ejercicio 1 - STRINGS
# ===================================   

nombre = "Juan"
print(nombre)

profesion = "Intructor"
print(profesion)

frase = "Estoy apredniendo python"
print(frase)

# ====================================
# Ejercicio 2 - LEN
# ====================================

nombre = "Juan"
print(len(nombre))

ciudad = "Envigado"
print(len(ciudad))


# ====================================
# Ejercicio 3 - IN
# ====================================

nombre = "Juan"
print("J" in nombre)
print("x" in nombre)

frase = "Estoy aprendiendo python"
print("python" in frase)

# ====================================
# Ejercicio 4 - INDICES
# ====================================

nombre = "Juan"
print(nombre[0])
print(nombre[2])
print(nombre[-1])

# ====================================
# Ejercicio 5 - INMUTABILIDAD
# ====================================

nombre = "Juan"
#nombre[0] = "P" # Esto no se puede hacer porque los strings son inmutables en una unica letra

nombre = "Juan"
nombre = "Puan"
print(nombre)

# ====================================
# Ejercicio 6 - CONCATENACION
# ====================================

nombre = "Juan"
apellido = "Muñoz"
print(nombre + " " + apellido)

nombre = "Juan"
nombre += " Esteban"
print(nombre)

# ====================================
# Ejercicio 7 - INTERPOLACION
# ====================================

nombre = "Juanes"
edad = 27
print(f"Mi nombre es {nombre} y tengo {edad} años")

# ====================================
# Ejercicio 8 - SLICING
# ====================================.

texto = "python"
print(texto[0:2]) #imprime "py"

texto = "python"
print(texto[2:6]) #imprime "thon"

texto = "python"
print(texto[:4]) #imprime "pyth"

texto = "python"
print(texto[3:]) #imprime "hon"

nombre = "Juan Esteban"
print(nombre[0:4]) #imprime "Juan"

nombre = "Juan Esteban"
print(nombre[5:]) #imprime "Esteban"

# ====================================
# Ejercicio 9 - STEP
# ====================================

texto = "python"
print(texto[::2]) #imprime "pto"
print(texto[::-1]) #imprime "nohtyp" 