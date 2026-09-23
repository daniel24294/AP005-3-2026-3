# 9) Imprimir los números primos existentes entre 0 y 30
tope_rango=30                         -> Define el límite superior del rango.
n = 0                                 -> Inicializa el número que se va a evaluar.
primo = True                          -> Supone inicialmente que el número es primo.
while (n < tope_rango):               -> Repite el proceso mientras n sea menor que 30.
    for div in range(2, n):           -> Prueba posibles divisores desde 2 hasta n-1.
        if (n % div == 0):            -> Comprueba si n es divisible exactamente por div.
            primo = False             -> Indica que n no es primo.
    if (primo):                       -> Comprueba si n resultó ser primo.
        print(n)                      -> Imprime el número primo.
    else:                             -> Se ejecuta cuando n no es primo.
        primo = True                  -> Reinicia la variable para evaluar el siguiente número.
    n += 1                            -> Incrementa n en 1.


# 10) ¿Se puede mejorar el proceso del punto 9? Utilizar las sentencias break y/ó continue para tal fin
n = 0                                 -> Reinicia el número que se va a evaluar.
primo = True                          -> Supone inicialmente que el número es primo.
while (n < tope_rango):               -> Repite el proceso mientras n sea menor que 30.
    for div in range(2, n):           -> Prueba posibles divisores desde 2 hasta n-1.
        if (n % div == 0):            -> Comprueba si n es divisible exactamente por div.
            primo = False             -> Indica que n no es primo.
            break                     -> Detiene el for al encontrar el primer divisor.
    if (primo):                       -> Comprueba si n es primo.
        print(n)                      -> Imprime el número primo.
    else:                             -> Se ejecuta cuando n no es primo.
        primo = True                  -> Reinicia la variable para la siguiente evaluación.
    n += 1                            -> Incrementa n en 1.


# 11) En los puntos 9 y 10, se diseño un código que encuentra números primos y además se lo optimizó. ¿Es posible saber en qué medida se optimizó?
ciclos_sin_break = 0                  -> Inicializa el contador de ciclos sin break.
n = 0                                 -> Reinicia el número a evaluar.
primo = True                          -> Supone inicialmente que el número es primo.
while (n < tope_rango):               -> Recorre los números menores que el límite.
    for div in range(2, n):           -> Prueba todos los posibles divisores.
        ciclos_sin_break += 1         -> Cuenta cada iteración realizada.
        if (n % div == 0):            -> Comprueba si div es divisor de n.
            primo = False             -> Indica que n no es primo.
    if (primo):                       -> Comprueba si n es primo.
        print(n)                      -> Imprime el número primo.
    else:                             -> Se ejecuta si n no es primo.
        primo = True                  -> Reinicia la variable primo.
    n += 1                            -> Incrementa n en 1.
print('Cantidad de ciclos: ' + str(ciclos_sin_break)) -> Muestra la cantidad total de ciclos sin break.


ciclos_con_break = 0                  -> Inicializa el contador de ciclos con break.
n = 0                                 -> Reinicia el número a evaluar.
primo = True                          -> Supone inicialmente que el número es primo.
while (n < tope_rango):               -> Recorre los números menores que el límite.
    for div in range(2, n):           -> Prueba posibles divisores.
        ciclos_con_break += 1         -> Cuenta cada iteración realizada.
        if (n % div == 0):            -> Comprueba si div es divisor de n.
            primo = False             -> Indica que n no es primo.
            break                     -> Detiene el ciclo al encontrar un divisor.
    if (primo):                       -> Comprueba si n es primo.
        print(n)                      -> Imprime el número primo.
    else:                             -> Se ejecuta si n no es primo.
        primo = True                  -> Reinicia la variable primo.
    n += 1                            -> Incrementa n en 1.
print('Cantidad de ciclos: ' + str(ciclos_con_break)) -> Muestra la cantidad total de ciclos con break.
print('Se optimizó a un ' + str(ciclos_con_break/ciclos_sin_break) + '% de ciclos aplicando break') -> Calcula la proporción de ciclos realizados con break respecto a los ciclos sin break.


# 12) Si la cantidad de números que se evalúa es mayor a treinta, esa optimización crece?
tope_rango=100                       -> Cambia el límite de evaluación a 100.
ciclos_sin_break = 0                 -> Reinicia el contador de ciclos sin break.
n = 0                                 -> Reinicia el número a evaluar.
primo = True                          -> Supone inicialmente que el número es primo.
while (n < tope_rango):               -> Recorre los números menores que 100.
    for div in range(2, n):           -> Prueba los posibles divisores de cada número.
        ciclos_sin_break += 1         -> Cuenta cada iteración realizada.
        if (n % div == 0):            -> Comprueba si div es divisor de n.
            primo = False             -> Indica que n no es primo.
    if (primo):                       -> Comprueba si n es primo.
        print(n)                      -> Imprime el número primo.
    else:                             -> Se ejecuta si n no es primo.
        primo = True                  -> Reinicia la variable primo.
    n += 1                            -> Incrementa n en 1.
print('Cantidad de ciclos: ' + str(ciclos_sin_break)) -> Muestra los ciclos realizados sin break.

ciclos_con_break = 0                  -> Reinicia el contador de ciclos con break.
n = 0                                 -> Reinicia el número a evaluar.
primo = True                          -> Supone inicialmente que el número es primo.
while (n < tope_rango):               -> Recorre los números menores que 100.
    for div in range(2, n):           -> Prueba los posibles divisores.
        ciclos_con_break += 1         -> Cuenta cada iteración realizada.
        if (n % div == 0):            -> Comprueba si div es divisor de n.
            primo = False             -> Indica que n no es primo.
            break                     -> Detiene el ciclo al encontrar el primer divisor.
    if (primo):                       -> Comprueba si n es primo.
        print(n)                      -> Imprime el número primo.
    else:                             -> Se ejecuta si n no es primo.
        primo = True                  -> Reinicia la variable primo.
    n += 1                            -> Incrementa n en 1.
print('Cantidad de ciclos: ' + str(ciclos_con_break)) -> Muestra los ciclos realizados con break.
print('Se optimizó a un ' + str(ciclos_con_break/ciclos_sin_break) + '% de ciclos aplicando break') -> Calcula la proporción de ciclos con break frente a los ciclos sin break.
