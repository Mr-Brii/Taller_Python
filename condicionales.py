
#crear variables
""""
print("por favor ingreselos siguentes datos\n")

var_nombre =  input("Nombre:")
var_edad = int(input("Edad: "))

#crear condicion

if var_edad < 0
    print ("Error")

elif var_edad >= 18  : 
    print(f"{var_nombre}  Eres Mayor de Edad.")
else:
    print(f"{var_nombre} Eres Menor de Edad.")
"""

#Ejemplo 2
"""
var_nombre = input("nombre")
var_notafinal = float(input("Nota Final: "))

if var_notafinal <= 0 or var_notafinal >5:
    print("Nota invalida")

elif var_notafinal >=4.5 and var_notafinal <= 5.0 : 
    print(f"Estudiante{var_notafinal} GANO (^_-)db(-_^) con Desempeño Excelente")

elif var_notafinal >=3.5 and var_notafinal <= 4.4 : 
    print(f"Estudiante{var_notafinal} GANO (^_-)db(-_^) con Desempeño Buen0")

elif var_notafinal >=3.0 and var_notafinal <= 3.4 : 
    print(f"Estudiante{var_notafinal} PERDIO (┬┬﹏┬┬)  con Desempeño Aceptable")

else:
    print(f"Estudiante{var_notafinal} PERDIO (┬┬﹏┬┬)  con Desempeño Insuficiente")
"""

#Ejemplo 3
'''
var_nombre = input("nombre")
var_valorDeCompra = float (input ("Compra"))

if var_valorDeCompra < 0 : 
    print(f"error")

elif var_valorDeCompra >=0 and var_valorDeCompra <= 100000 :
    print (f"""
    -cliente {var_nombre} 
    -compra {var_valorDeCompra}
    """)

elif  var_valorDeCompra >= 100000 and var_valorDeCompra < 300000 :
    print(f"Compra mayor a {var_valorDeCompra} se aplica 10% ")
    var_descuento = ( var_valorDeCompra * 0.10)
    var_valorAPagar = var_valorDeCompra - var_descuento

    print(f"""
    -cliente {var_nombre} 
    -compra de {var_valorDeCompra}
    -Descuento de 10%{var_descuento}
    -total a pagar es:{int(var_valorAPagar)}
    """)

elif var_valorDeCompra >= 300000 and var_valorDeCompra < 500000 :
    print(f"Compra mayor a {var_valorDeCompra} se aplica 15% ")
    var_descuento = ( var_valorDeCompra * 0.15)
    var_valorAPagar = var_valorDeCompra - var_descuento

    print(f"""
    -cliente {var_nombre} 
    -compra de {var_valorDeCompra}
    -Descuento de 15%{var_descuento}
    -total a pagar es:{int(var_valorAPagar)}
    """)

else: 
    print(f"Compra mayor a {var_valorDeCompra} se aplica 20% ")
    var_descuento = (var_valorDeCompra * 0.20)
    var_valorAPagar = var_valorDeCompra - var_descuento

    print(f"""
    -cliente {var_nombre} 
    -compra de {var_valorDeCompra}
    -Descuento de 20%{var_descuento}
    -total a pagar es:{int(var_valorAPagar)}
    """)
'''
#Ejercicio 4 Temperatura 

'''
print("Ejercicio: Temperatura")

ciudad = input("Ingrese el nombre de la ciudad: ")
temperatura = float(input("Ingrese la temperatura actual en °C: "))

if temperatura < 10:
    clasificacion = "Muy fría"
elif temperatura >= 10 and temperatura <= 17:
    clasificacion = "Fría"
elif temperatura >= 18 and temperatura <= 25:
    clasificacion = "Templada"
elif temperatura >= 26 and temperatura <= 32:
    clasificacion = "Caliente"
else:
    clasificacion = "Muy caliente"

if temperatura < 18:
    recomendacion = "Se recomienda llevar abrigo."
else:
    recomendacion = "No es necesario llevar abrigo."

print(f"""
-Ciudad: {ciudad}
-Temperatura: {temperatura} °C
-Clasificación: {clasificacion}
-Recomendación: {recomendacion}
""")
'''

#Ejercicio 5 

'''
print("Ejercicio: Valor horas")
nombre = input("Ingrese el nombre del empleado: ")

horas = float(input("Ingrese las horas trabajadas durante el mes: "))
valor_hora = float(input("Ingrese el valor de la hora normal: "))

if horas <= 0 or valor_hora <= 0:
    print("Error: las horas trabajadas y el valor de la hora deben ser positivos.")
else:
    if horas <= 160:
        horas_normales = horas
        horas_extra = 0
    else:
        horas_normales = 160
        horas_extra = horas - 160

    pago_horas_normales = horas_normales * valor_hora
    valor_hora_extra = valor_hora * 1.25
    pago_horas_extra = horas_extra * valor_hora_extra

    salario_bruto = pago_horas_normales + pago_horas_extra

    descuento = salario_bruto * 0.08

    salario_neto = salario_bruto - descuento

    print(f"""
    -Empleado: {nombre}
    -Horas normales: {horas_normales}
    -Horas extra: {horas_extra}
    -Pago por hora normal: {valor_hora}
    -Pago por hora extra: {valor_hora_extra}
    -Salario total (bruto): {salario_bruto}
    -Descuento de salud y pensión (8%): {descuento}
    -Salario neto: {salario_neto}
    """)
'''
