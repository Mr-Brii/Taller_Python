'''
for i in range (2, 11, 2):
    print(f"{i} Dracarys 🔥")
'''
'''
mensaje = input ("Escribe tu mensaje : ")
repeticion = int(input("Cuantas veces quieres repetir este mensaje : "))

for i in range (repeticion): 
    print(f"{i+1} - {mensaje}")
'''
#Preguntar al profe: Cuantas notas quiere registrar
#hacer el promedio de las notas y mostrarlo 
#promedio >=3.5 Mostrar Estudiante Gano - contrario perdio 
'''
print("=== Sistema de calificacion. ===")
Estudiante = input("Nombre del Estudiante : ")
Can_notas = int(input("Cuantas notas vas a registrar : "))

Promedio = 0
for i in range (Can_notas):
    notas=float(input(f"Ingrese nota {1+1} : "))
    if notas not in range (0,5) : 
        print("Nota invalida")
        break
    Promedio +=notas

Promedio_Final = Promedio/Can_notas

if (Promedio/Can_notas) >=3.5: 
    print (f"El Estudiante {Estudiante} - promedio {Promedio_Final:.1F} Gano 🎉")
else:
    print (f"El Estudiante {Estudiante} - promedio {Promedio_Final:.1F} Perdio ❌")
'''
'''
while True: 
    menu = int(input("""
    Seleccione Opcion a realizar : 

    1. Sumar
    2. Restar 
    3. Salir
    :   """))

    if menu == 1: 
        n1 = int(input("Ingrese N1 :"))
        n2 = int(input("Ingrese N2 :"))
        print (f"resultado {n1+n2}")

    elif menu == 2: 
        n1 = int(input("Ingrese N1 :"))
        n2 = int(input("Ingrese N2 :"))
        print (f"resultado {n1+n2}")

    elif menu == 3: 
        print("salida del sistema")
        break
    else: 
        print("Opcion Invalida")
'''

