# Instituto Tecnologico de Costa Rica
# Microprocesadores y Microcontroladores MT-7003
# Tarea 1: GitHub, Pytest y Flake 8
# Profesor: Ing. Rodolfo Piedra Camacho
# Estudiante 1: Alejandra Sousa Leal
# Estudiante 2: David Wu Cen
# Seccion Practica

# Metodo multiple_op
def multiple_op(numero):  # entrada de un parametro numerico
    multiplicacion = 0  # variables de las 3 operaciones
    potencia = 0
    factorial = 1
    if numero.isnumeric() is True:  # verificacion caracter numerico
        print("Su numero es: ", numero)  # muestra el numero ingresado
        num = int(numero)  # pasamos a int para operaciones matematicas
        multiplicacion = num*num
        potencia = 2**num
        for i in range(1, num+1):  # loop de factorial
            factorial = factorial*i
        # lista se usa para mostrar operaciones y resultados
        numstr = str(num)  # se pasa a string para poder hacer display
        lista = [numstr+"*"+numstr, "2^"+numstr, numstr+"!"]
        print("Operaciones: ", lista)  # se muestran las operaciones
        lista = [multiplicacion, potencia, factorial]  # se asignan resultados
        return lista  # retornamos la lista
    else:
        print("Su caracter es: "+numero)  # mostramos el caracter equivocado
        return 11  # retornamos un codigo de error


# Metodo verify_array_op
def verify_array_op(numlist):  # recibe un array de caracteres
    print("El array ingresado es: ", numlist)  # muestra la lista ingresada
    for i in range(5):  # verificacion numerica, recorre la lista en loop
        if numlist[i].isnumeric() is False:  # ver si el elemento es numerico
            print("Se detecto un caracter que no es un numero positivo.")
            return 13  # si no es numerico retorna un error
    nummatriz = []  # aca almacenamos los resultados
    for i in range(5):  # llama multiple_op para cada num
        nummatriz.append(multiple_op(numlist[i]))
    print("Array de arrays resultante: ")
    return nummatriz  # retorna el array de arrays
