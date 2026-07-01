""" Crea un planificador meteorológico para viajes.
En este laboratorio, utilizarás sentencias condicionales para determinar si es posible desplazarse al trabajo en función del clima, la distancia a recorrer y la disponibilidad de un vehículo.

Objetivo: Cumplir con las historias de usuario que se detallan a continuación y lograr que todas las pruebas se superen para completar el laboratorio.

Historias de usuario:

Debes crear las siguientes variables:
distance_mi(un número que representa la distancia a recorrer en millas)
is_raining(un valor booleano que indica si el usuario está experimentando actualmente un clima lluvioso)
has_bike(un valor booleano que indica si el usuario tiene una bicicleta)
has_car(un valor booleano que indica si el usuario tiene un coche)
has_ride_share_app(un valor booleano que indica si el usuario tiene una aplicación que le permite solicitar un viaje)
Debes utilizar sentencias condicionales para determinar si es posible desplazarse al trabajo en función de los valores de estas variables.
Debe utilizar las declaraciones if, elif, y elsepara evaluar las categorías de distancia en orden ascendente.
Si distance_mies un valor falso:
Debes imprimir False.
Si la distancia es menor o igual a 1 milla :
Solo debes imprimir Truesi no está lloviendo .
De lo contrario, deberías imprimir False.
Si la distancia es mayor que 1 milla y menor o igual a 6 millas :
Solo debes imprimir Truesi la persona tiene una bicicleta y no está lloviendo.
De lo contrario, deberías imprimir False.
Si la distancia es mayor a 6 millas :
Debes imprimirlo Truesi la persona tiene coche o utiliza una aplicación de transporte compartido.
De lo contrario, deberías imprimir False. """

distance_mi = 6
is_raining = False
has_bike = True
has_car = False
has_ride_share_app = True

if not distance_mi:
    print(False)

elif distance_mi <= 1:
    if not is_raining:
        print(True)
    else:
        print(False)

elif distance_mi > 1 and distance_mi <= 6:
    if has_bike and not is_raining:
        print(True)
    else:
        print(False)

elif distance_mi > 6:
    if has_car or has_ride_share_app:
        print(True)
    else:
        print(False)