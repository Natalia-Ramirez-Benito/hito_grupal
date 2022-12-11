from random import sample 
# Importamos un metodo de la biblioteca random para generar listas aleatorias

lista = list(range(1, 11))  # Creamos la lista base con números del 1 al 10

# Creamos una lista aleatoria de largo 10 para cada método de ordenación
vectorburbuja = sample(lista, 10)
vectorselect = sample(lista, 10)
vectorinsert = sample(lista, 10)
vectorshell = sample(lista, 10)


def bubblesort(vectorburbuja):
    # Imprimimos la lista desordenada
    print("----------------------------------------------------------------------")
    print(f'El vector antes de ordenar: {vectorburbuja}')

    for i in range(len(vectorburbuja)-1):  # Le damos un rango n para que complete el proceso.
        for j in range(0, len(vectorburbuja)-i-1):
            # Revisa la matriz de 0 hasta n-i-1
            if vectorburbuja[j] > vectorburbuja[j+1]:
                # Cambia los elementos
                vectorburbuja[j], vectorburbuja[j+1] = vectorburbuja[j+1], vectorburbuja[j]
    # imprimimos la lista ordenada con el método bubble sort
    print(f'El vector ordenado con bubble es: {vectorburbuja}')


def insertsort(vectorinsert):
    # Imprimimos la lista desordenada
    print("----------------------------------------------------------------------")
    print(f'El vector a ordenar con inserción es: {vectorinsert}')

    # Comience en el segundo elemento ya que asumimos que el primer elemento está ordenado
    for i in range(1, len(vectorinsert)):
        numero_insertar = vectorinsert[i]
        # Mantenemos una referencia del índice del elemento anterior.
        j = i - 1
        # Movemos todos los elementos del segmento ordenado hacia adelante si son más grandes que
        # el elemento a insertar
        while j >= 0 and vectorinsert[j] > numero_insertar:
            vectorinsert[j + 1] = vectorinsert[j]
            j -= 1
        # Insertamos el elemento
        vectorinsert[j + 1] = numero_insertar

    print(f'El vector ordenado con inserción es: {vectorinsert}')


def selectsort(vectorselect):
    # Imprimimos la lista desordenada
    print("----------------------------------------------------------------------")
    print(f'El vector antes de ordenar: {vectorselect}')
        
    for i in range(len(vectorselect)):
        # Encontrar el minimo elemento de los restantes sin ordenar
        minimo = i 
        for j in range(i+1, len(vectorselect)):
            if vectorselect[minimo] > vectorselect[j]: 
                minimo = j
        # Cambiamos el elemento minimo encontrado con el primer elemento de la matriz
        vectorselect[i], vectorselect[minimo] = vectorselect[minimo], vectorselect[i]
        # Repetimos el proceso hasta terminar

    print(f'El vector ordenado con el método select sort es: {vectorselect}')


def shellsort(vectorshell):
    # Imprimimos la lista desordenada
    print("----------------------------------------------------------------------")
    print(f'El vector a ordenar con shell es: {vectorshell}')

    distancia = len(vectorshell) // 2
    
     # Creamos un bucle según las distancias
    while distancia > 0:
        # Utilizamos el Insertionsort
        for i in range(distancia, len(vectorshell)):
            numero = vectorshell[i]
            j = i
            while j >= distancia and vectorshell[j - distancia] > numero:
                vectorshell[j] = vectorshell[j - distancia]
                j -= distancia
            vectorshell[j] = numero
        distancia //= 2  # Acotamos la distancia nuevamente y continua el ciclo
    print(f'El vector ordenado con shell es: {vectorshell}')


bubblesort(vectorburbuja)
selectsort(vectorselect)
insertsort(vectorinsert)
shellsort(vectorshell)
