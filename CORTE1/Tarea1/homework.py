a = input("Enter a number: ")              -> Solicita al usuario un número y lo guarda como texto.
a = int(a)                                -> Convierte a a un número entero.
b = input("Enter b number: ")             -> Solicita al usuario otro número y lo guarda como texto.
b = float(b)                               -> Convierte b a un número decimal.
c = a + b                                 -> Suma los valores de a y b.

if a == b:                                 -> Comprueba si a y b tienen el mismo valor.
    print("equal")                         -> Imprime "equal" si son iguales.
else:                                      -> Se ejecuta si los valores son diferentes.
    print("Different")                    -> Imprime "Different" si no son iguales.

print("Type of a is: ", type(a))           -> Muestra el tipo de dato de a.
print("Type of b is: ", type(b))           -> Muestra el tipo de dato de b.
print("c = ", c)                           -> Muestra el resultado de la suma.

if type(a) == type(b):                     -> Comprueba si a y b son del mismo tipo de dato.
    print("a and b are of the same type")  -> Indica que ambos tienen el mismo tipo.
else:                                      -> Se ejecuta si tienen tipos diferentes.
    print("a and b are of different type")-> Indica que tienen tipos diferentes.
