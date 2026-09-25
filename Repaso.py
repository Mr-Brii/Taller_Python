#Variables
print("=== Teinda Donde Ely ===")

print("Por favor ingrese la siguiente informacion: \n")
Cliente = input("Nombre de cliente: ")
Producto = input("Nombre de producto: ")
Cantidad = int(input("Cantidad : "))
Precio = float(input("Precio: "))

#Variable para preguntar si la compra es a domicilio 
Domicilio = input("La compra es para domicilio (SI - NO): ")

#Condicion verificar que respondio el usuuario 

#.upper() Convierte en mayuscula .lower() minuscula 
if Domicilio.upper() == "NO":
    print("=== RESUMEN COMPRA ===")
    print(f"""
    - Cliente : {Cliente}
    - Producto : {Producto}
    - Cantidad : {Cantidad}
    - Total :  {Cantidad*Precio}

    🛒Gracias por su compra.🛒
    """)  
elif Domicilio.upper() == "SI":
    Direccion=input("Ingrese Municipio de envio: (Medellín, Itagui, Bello): ")

    Valor_Domicilio=0
    if Direccion.lower()== "medellin": 
        Valor_Domicilio =5000
    elif Direccion.lower()== "itagui":
        Valor_Domicilio =10000
    elif Direccion.lower()== "bello":
        Valor_Domicilio =8000
    else:
        print("Direccion Invalida")

#Resumen de lva venta 

    print("=== RESUMEN COMPRA ===")
    print(f"""
    - Cliente : {Cliente}
    - Producto : {Producto}
    - Cantidad : {Cantidad}
    - Precio :  {Precio}
    - Subtotal : {Cantidad*Precio}
    - Domicilio : {Domicilio}
    - Total pagar : {Valor_Domicilio + (Cantidad*Precio)}

    🛒Gracias por su compra.🛒
    """)  

else: 
    print ("Opcion Invalida")
    