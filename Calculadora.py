def realizar_operacion (operacion, numero1, numero2) :
    if operacion == 1:
        return numero1 + numero2
    elif operacion == 2 :
        return numero1 - numero2
    elif operacion == 3 :
        return numero1 * numero2
    elif operacion == 4 :
        return numero1 / numero2
    else:
        return  numero1 // numero2

print("--- Bienvenido a la Calculadora en Python ---")
while True:
    print("\nPuedo realizar las siguientes operaciones, escoge una:")
    print("\n1 - Suma")
    print("\n2 - Resta")
    print("\n3 - Multiplicación")
    print("\n4 - División")
    print("\n5 - División Entera\n")

    try:
        operacion = int (input("Introduce el número de operación que quieres realizar: "))
        numero1 = int (input("\nIntroduce el primer número: "))
        numero2 = int (input("\nIntroduce el segundo número: "))

    except ValueError:
        print("Por favor, introduce solo números")
    else:
        if operacion < 1 or operacion > 5:
            print("\n --- Ese no es un número de operación valido ---")
            continue
        resultado = realizar_operacion(operacion, numero1, numero2)
        print("\nEl resultado es: " + str (resultado))
        continuar = input("\n---- ¿Deseas continuar? -----\n\n Si / No ")
        print()
        print()
        if continuar != "si":
            break

print("--- 'Gracias por usar nuestra calculadora!' ---")
