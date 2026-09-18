print("ejercicio 1: suma de dos numeros")
print("--"*20)

Numero1= float(input("Ingrese el primer numero"))
numero2 = float(input("Ingrese el segundo número:"))

print(f"Resultado: {Numero1+numero2}")

print("Ejercicio 2: area de un rectangulo")

Base = float(input ("ingrese la base del rectangulo:"))
altura = float(input("ingrese la altura del rectangulo"))

area = Base * altura   # fórmula: base × altura

print(f"El área del rectángulo es: {area}")

print (f"Ejercicio 3: Conversión de minutos a horas y minutos")

minutos_totales = int(input("Ingrese la cantidad de minutos: "))

horas   = minutos_totales // 60   # división entera → horas completas
minutos = minutos_totales % 60    # módulo → minutos restantes

print(f"{minutos_totales} minutos equivalen a {horas} horas y {minutos} minutos")