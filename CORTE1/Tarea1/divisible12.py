for i in range(100, 301):  -> Recorre los números del 100 al 300.
    if (i%12) != 0:        -> Verifica si i no es divisible entre 12.
        continue           -> Salta a la siguiente iteración.
    print(i)               -> Imprime los números divisibles entre 12.
