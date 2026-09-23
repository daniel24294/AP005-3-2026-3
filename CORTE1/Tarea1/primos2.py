a = 1                                      -> Inicializa a en 1 para controlar la repetición del programa.
value = input('Ingrese un valor')          -> Solicita al usuario un valor.
value = int(value)                         -> Convierte el valor ingresado a entero.

while a == 1:                              -> Repite el programa mientras a sea igual a 1.
    for i in range(1,value+1):             -> Recorre los números desde 1 hasta value.
        conta = 0                          -> Reinicia el contador de divisores para cada número.
        for n in range(1, i+1):            -> Recorre los posibles divisores de i.
            residue = i%n                  -> Calcula el residuo de dividir i entre n.
            if residue == 0:               -> Comprueba si n divide exactamente a i.
                conta = conta + 1          -> Aumenta el contador de divisores.
            
            # print("i = ", i)             -> Mostraría el valor actual de i.
            # print("n = ", n)             -> Mostraría el valor actual de n.
            # print("residue = ", residue) -> Mostraría el residuo de la división.
            # print("conta = ", conta)     -> Mostraría la cantidad de divisores encontrados.
    if conta == 2:                         -> Comprueba si el último i tiene exactamente dos divisores.
       print(f'{i} es un primo')            -> Indica que el número es primo.
       print("\n")                          -> Imprime saltos de línea.
    else:                                   -> Se ejecuta si el último i no tiene dos divisores.
       print(f'{i} NOOO es un primo')       -> Indica que el número no es primo.
       print("\n")                          -> Imprime saltos de línea.

    print('Do you want to continue?. Press 1 to do that') -> Pregunta si se desea repetir el programa.
    a = input()                             -> Lee la respuesta del usuario.
    a = int(a)                              -> Convierte la respuesta a entero.

    if a != 1:                              -> Comprueba si el usuario decidió no continuar.
        break                               -> Termina el ciclo while.

    value = input('Ingrese un valor')       -> Solicita un nuevo valor para repetir el proceso.
    value = int(value)                     -> Convierte el nuevo valor a entero.
