#Repaso Ciclos. 
'''
lista_producto=[] #Lista en blanco 
Cantidad = int(input("Cantidad de productos a comprar: "))

for i in range(Cantidad): 
    Producto=input(f"Nombre del producto {i+i}: ")
    #agregar producto a la lista
    lista_producto.append(Producto)
print(f"Productos comprdos:{lista_producto}")
'''
Lista_Perros=[]
Lista_Gatos=[]
while True: 
    pregunta=int(input("""
    1. Registrar Perros 🐶
    2. Registrar Gatos 😸
    3. Listado perros 🦮
    4. Listado Gatos 🐈
    5. Salir
"""))

    if pregunta ==1: 
       Perro= input("Ingrese nombre del perro: ")
       Lista_Perros.append(Perro)
       print("Perro Registrado")

    elif pregunta ==2: 
        Gato= input("Ingrese nombre del gato: ")
        Lista_Gatos.append(Gato)
        print("Gato Registrado")

    elif pregunta ==3: 
       print("listado de perros", Lista_Perros)

    elif pregunta ==4:
        print("listado de gatos", Lista_Gatos)

    elif pregunta ==5
        print("Saliendo del sistema")
        break
    else: 
        print("Opcion invalida")
        break
    