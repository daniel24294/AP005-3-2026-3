import time                              -> Importa el módulo time para medir el tiempo de ejecución.
inicio = time.time()                     -> Guarda el tiempo inicial.

for i in range(1,31):                    -> Recorre los números del 1 al 30.
    conta = 0                            -> Inicializa el contador de divisores en 0.
    for n in range(1, i+1):              -> Recorre los posibles divisores de i desde 1 hasta i.
        residue = i%n                    -> Calcula el residuo de dividir i entre n.
        if residue == 0:                 -> Comprueba si n es divisor exacto de i.
            conta = conta + 1            -> Aumenta en 1 el número de divisores encontrados.
    if conta == 2:                       -> Verifica si i tiene exactamente dos divisores.
        print(f'{i} es un primo')        -> Imprime i indicando que es un número primo.
        print("\n")                      -> Imprime un salto de línea adicional.

fin = time.time()                        -> Guarda el tiempo final de ejecución.
print("t = ", (fin - inicio)*1000)       -> Calcula y muestra el tiempo de ejecución en milisegundos.
