# for i in range (1,21):                  -> Recorre los números del 1 al 20.
#     residual = i%2                      -> Calcula el residuo de dividir i entre 2.
#     if residual == 0:                   -> Verifica si el número es par.
#         print(f'{i} is even')           -> Imprime que el número es par.
#     else:                               -> Se ejecuta si el número no es par.
#         #print(f'{i} is odd')           -> Imprimiría que el número es impar.
#         print(str(i) + ' is odd')       -> Convierte i a texto y muestra que es impar.

# for i in range (0,6):                   -> Recorre los números del 0 al 5.
#     result = i**3                       -> Calcula el cubo de i.
#     print(result)                       -> Imprime el resultado.

times = input("Enter a number of times: ") -> Solicita al usuario un número de repeticiones.
times = float(times)                       -> Convierte el valor ingresado a decimal.
times = int(times)                         -> Convierte el valor decimal a entero.
print(type(times))                         -> Muestra el tipo de dato de times.
print(times)                               -> Muestra el valor de times.

if times == 0:                             -> Comprueba si times es igual a 0.
    print("Don't do anything")             -> Indica que no se realizará ninguna acción.
else:                                      -> Se ejecuta cuando times es diferente de 0.
    for i in range(1,times+1):             -> Recorre los números desde 1 hasta times.
        print("i = ", i)                   -> Imprime el valor actual de i.
