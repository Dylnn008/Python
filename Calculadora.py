#Calculadora
#Crear funcion que permita realizar operaciones basicas
def calculadora():
    print("Seleccione la operacion que desea realizar:")
    operaciones_basicas = {1: 'Suma', 2: 'Resta', 3: 'Multiplicacion', 4: 'Division'}
    for clave, valor in operaciones_basicas.items():
        print(f"{clave}. {valor}")
    operacion = int(input("Ingrese el numero de la operacion (1/2/3/4): "))
    if operacion not in operaciones_basicas:
        return "Operacion no valida."
    num1 = float(input("Ingrese el primer numero: "))
    num2 = float(input("Ingrese el segundo numero: "))
    if operacion == 1:
        return f"{num1 + num2}"
    elif operacion == 2:
        return f"{num1 - num2}"
    elif operacion == 3:
        return f"{num1 * num2}"
    elif operacion == 4:
        if num2 != 0:
            return f"{num1 / num2}"
        else:
            return "Error: Division por cero no es permitida."
    else:
        return "Operacion no valida."
print(calculadora())