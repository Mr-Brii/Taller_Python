while True:
    try:
        nota=float(input("Ingresa una nota"))
    except ValueError: 
        print("Ingresa una nota valida. ")