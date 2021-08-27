# Instituto Tecnologico de Costa RIca
# Microprocesadores y MIcrocontroladores MT-7003
# Tarea 2: Manejo de Maquinas Virtuales
# Profesor: Ing. Rodolfo Piedra Camacho
# Integrantes: David Wu Cen y Alejandra Sousa Leal


import random                                                                                               # Utilizado para crear la lista aleatoriamente
import time                                                                                                 # Utilizado para medir el tiempo de ejecucion
import multiprocessing                                                                                      # Para poder usar multithreading
import argparse                                                                                             # Para poder pasar argumentos desde el Shell


parser = argparse.ArgumentParser(description = 'Obtener las potencias de todos los numeros de un array')    # Creamos un parser para almacenar los argumentos y le ponemos descripcion

parser.add_argument('-l', '--largo', type = int, metavar = '', required = True, help = 'Largo del array')   # Creamos un argumento de largo del array, tipo int, de entrada obligatoria
parser.add_argument('-t', '--texto', action = 'store_true', help = 'Bandera para guardado en archivo txt')  # Creamos una bandera opcional para escribir los tiempos a un txt

args = parser.parse_args()                                                                                  # Se asignan los argumentos del parser a args


def generararray(size):                                                                                     # Recibe como parametro el tamano del array
    lista = [None] * size                                                                                   # Rellena de caracteres nulos
    for i in range(0, size):                                                                                # Loop para llenar la lista con numeros aleatorios de 25 a 100
        lista[i] = random.randint(25, 250)
    return lista


def potencia_individual(numero):
    temp = numero*numero
    return temp


def tiempos(texto, start_single, finish_single, start_multi, finish_multi):                                 # Cuatro parametros de entrada, la bandera de texto y los 4 tiempos, iniciales y finales, single y multithreaded
    if (texto == False):                                                                                    # Si no se da la bandera de texto, por default, imprimimos los tiempos
        print(f'Se tardo {finish_single - start_single} segundo(s) en singlethreaded')
        print(f'Se tardo {finish_multi - start_multi} segundo(s) en multithreaded')
    else:
        file = open("TIempos.txt", "w")                                                                     # Si se provee la bandera, abrimos el archivo, o lo creamos si no existe

        file.write(f'Se tardo {finish_single - start_single} segundo(s) en singlethreaded\n')               # Escribimos los tiempos para single y multithreading
        file.write(f'Se tardo {finish_multi - start_multi} segundo(s) en multithreaded\n')

        file.close()                                                                                        # Cerramos el archivo


def main():                                                                                                 # Definimos el main, es decir, desde donde llamaremos todas nuestras funciones
    numeros = generararray(args.largo)                                                                      # Se llama para la creacion del array con el parametro largo

    pool_single = multiprocessing.Pool(processes = 1)                                                       # Se establece un pool, con un solo hilo

    start_single  = time.perf_counter()                                                                     # Se empieza a contar el tiempo

    pool_single .map(potencia_individual, numeros)                                                          # Para la funcion potencia_individual se pasan todos los elementos de numeros

    pool_single .close()                                                                                    # Se cierra el pool
    pool_single .join()                                                                                     # Se utiliza para que no corra codigo despues de este punto hasta que termine la ejecucion del pool

    finish_single  = time.perf_counter()                                                                    # Se termina de contar el tiempo

    pool_multi = multiprocessing.Pool(processes = 4)                                                        # Se establecen 4 hilos en lugar de 1

    start_multi = time.perf_counter()

    pool_multi.map(potencia_individual, numeros)

    pool_multi.close()
    pool_multi.join()

    finish_multi = time.perf_counter()

    tiempos(args.texto, start_single, finish_single, start_multi, finish_multi)                             # Se pasa a la funcion de tiempos para saber si imprimimos o guardamos en txt


if (__name__ == '__main__'):
    main()                                                                                                  # Llamamos al main
