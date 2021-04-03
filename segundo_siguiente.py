
#Tarea: 16, estructuras ded decisión, Siguiente segundo.
#Autor: Diego Ochoa Camarena.
#Fecha de entrega: 25/03/2021
#Grupo: ESI-232A4
#profesor: JORGE ADALBERTO ZALDIVAR CARRILLO.

#Descripción:
# El programa recibirá tres números enteros que representarán,
#respectivamente, las horas, minutos y segundos correpondientes
#a un momento dado.
# El programa calculará, a continuación, la hora correspondiente
#al siguiente segundo, es decir, qué hora sería una vez que ha
#transcurrido un segundo después de la hora proporcionada como entrada.


print("Porfavor ingrese una hora la cual es en formato militar,")
print(" es decir 24hrs, un minuto y un segundo")
#Entrada
    #Esto es mi hora inicial.
hora = int(input("Ingrese una hora en formato de 24hrs.: "))
minuto = int(input("Ingrese un minuto: "))
segundo = int(input("Ingrese un segundo: "))

#Proceso
# A las variables les agregare un número "1",
#puesto que es la cantidad de segundos a agregar,
#esto con el fin de no perder un orden, o bien tener una mejor logica,
#detras del nombre de la vraiable.
if segundo == 59:
    hora1 = hora
    segundo1 = 0
    minuto1 = minuto + 1
    if minuto1 == 60:
        minuto1  = 0
        hora1 = hora + 1
        if hora1 == 24:
            hora1 = 0
    else:
        hora1 = hora
else:
    segundo1 = segundo + 1
    minuto1 = minuto
    hora1 = hora


#Salida
    #Esto es mi hora final.
print(hora1,"h", minuto1,"m", segundo1,"s")
