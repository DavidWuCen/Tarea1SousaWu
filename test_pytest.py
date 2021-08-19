import Tarea1SousaWu as t  # importar el codigo de funciones
import random  # importar la libreria random
# ERR1x2 -3 Los casos negativos si esperan el codigo de error dado
# ERR2x2 -5 Los casos positivos no me prueban que las operaciones se dieran
# bien

e11 = "Se detecto un caracter que no es un numero positivo"  # mensaje error 11
e13 = "Se detecto un caracter que no es un numero positivo"  # mensaje error 13


# test para el caso exitoso de multiple_op
def test_multiple_op_exito():
    # se llama multiple_op con un numero random del 1 al 10
    x = t.multiple_op(str(random.randint(1, 10)))
    # si se obtiene el error 11, da el mensaje de error
    assert x != 11, ("Error 11: NO_POS_NUM_CHAR " + e11)


# test para el caso exitoso de verify_array_op
def test_verify_array_op_exito():
    lista = []  # se crea una lista que se pasara al metodo
    for i in range(5):  # loop para asignar valores a la lista
        # se asigna a una variable un numero random del 1 al 10
        a = str(random.randint(1, 10))
        # se le asigna el valor a la lista
        lista.append(a)
    # en este punto toda la lista son numeros enteros
    x = t.verify_array_op(lista)
    # si se obtiene el error 13, da el mensaje de error
    assert x != 13, ("Error 13: ARRAY_NO_POS_NUM_CHAR " + e13)


# test para el caso negativo de multiple_op
def test_multiple_op_negativo():
    # genera un codigo ASCII de letra mayusculas para el metodo
    x = t.multiple_op(chr(random.randint(65, 90)))
    # si se obtiene el error 11, da el mensaje de error
    assert x != 11, ("Error 11: NO_POS_NUM_CHAR " + e11)


# test para el caso negativo de verify_array_op
def test_verify_array_op_negativo():
    lista = []  # se crea una lista para almacenar valores
    for i in range(5):  # se hace un loop para llenar la lista
        a = str(random.randint(1, 10))
        # se agrega a la lista
        lista.append(a)
    # b aca es un indica aleatorio de la lista
    b = random.randint(0, 4)
    # se le asigna a la posicion b de la lista una letra random
    lista[b] = chr(random.randint(65, 90))
    # se pasa la lista al metodo
    x = t.verify_array_op(lista)
    # si se obtiene el error 13, da el mensaje de error
    assert x != 13, ("Error 13: ARRAY_NO_POS_NUM_CHAR " + e13)
