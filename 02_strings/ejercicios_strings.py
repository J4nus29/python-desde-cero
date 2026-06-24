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

# ====================================
# Ejercicio 10 - METODOS DE STRINGS
# ====================================  

nombre = "juan"
print(nombre.upper()) # Hace que todas las letras sean mayusculas

nombre = "JUAN"
print(nombre.lower()) # Hace que todas las letras sean minusculas

nombre = " Juan Esteban " # Elimina los espacios al inicio y al final
print(nombre.strip())

frase = "Me gusta python"
print(frase.replace("python", "java")) # Reemplaza la palabra python por java

frase = "banana"
print(frase.count("a")) # Cuenta cuantas veces aparece la letra "a" en la frase

# ====================================
# Ejercicio 11 - MÁS METODOS DE STRINGS
# ====================================

texto = "Juan Esteban Muñoz"
print(texto.split()) # Convierte el string en una lista de palabras

texto = "Python"
print(texto.find("h")) # Indica en qué índice se encuentra el texto buscado

texto = "Python"
print(texto.startswith("Py")) # Indica si la frase comienza con el argumento que le dimos

texto = "Python"
print(texto.endswith("on")) # Indica si la frase termina con el argumento que le dimos

texto = "Python"
print(texto.find("z"))

# ====================================
# EJERCICIO 12 - ULTIMOS METODOS
# ====================================

texto = "juan esteban"
print(texto.capitalize()) # Primer letra mayuscula y las demas minusculas

texto = "PYTHON"
print(texto.isupper()) # Verifica que todo este en mayusculas y responde con un TRUE o FALSE

texto = "python"
print(texto.islower()) # Verifica que todo este en minusculas y responde con un TRUE o FALSE

texto = "juan esteban muñoz"
print(texto.title()) # Pone la primer letra de cada frase en mayuscula

nombres = ["Juan", "Esteban", "Muñoz"]
print(" ".join(nombres)) # Unir las palabras de una lista en un solo texto

