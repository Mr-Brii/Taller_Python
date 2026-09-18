
#Cracion de variables
nombre = "Brii"
documento    = 1000         # Variable de tipo entero (número entero)
direccion    = "Medellin, Barrio Santacho"  # Variable de tipo string (cadena de texto)
tiene_deudas = True        

#Mostrar informacion en pantalla 
print(nombre)

# CONCATENACIÓN USANDO +
print("CONCATENACIÓN USANDO +")
print("=" * 30)

#Opcion 1: Usando "+" No recomendable
print("Mi nombre es: " + nombre + "Mi documento es" + str (documento))

#Opcion 2: usando "coma"

print("Mi nombre es:", nombre, "Mi documento es:", documento, "Mi direccion es:", direccion, "Mi deuda es", tiene_deudas)

#Opcion 3: Usando "F" recomendado 

print(f"Mi nombre es: {nombre} Mi documento es: {documento} Mi direccion es {direccion} Mi deuda es {tiene_deudas}")

#Opcion 4: usando "f y comillas"

print(f"""
Nombre:             {nombre}
documento           {documento}
Direccion:          {direccion}
Tiene deudas:       {tiene_deudas}
""")

print(f"\n Hola, {nombre}!")

print(f"Bienvenido {nombre} a Python.\n")


