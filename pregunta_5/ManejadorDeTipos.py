"""
Programa manejador de tipos de datos
Permite definir tipos atomicos, registros struct
y registros varientes unions
"""

import sys

"""
Dada la accion a realizar, la ejecuta
segun los argumentos introducidos por el usuario
"""
def ejecutar(tipo, argumentos, memoria):
    if(tipo == "ATOMICO"):
        atomico(argumentos, memoria)
    elif(tipo == "STRUCT"):
        struct(argumentos, memoria)
    elif( tipo == "UNION"):
        union(argumentos, memoria)
    elif( tipo == "DESCRIBIR" ):
        describir(argumentos, memoria)
    elif(accion == "SALIR"):
        sys.exit()

"""
Se define un tipo de dato atomico. Estos 
tipos de datos don los que pueden conformar un
struct o un union.

Segun la documentacion del examen:

Define un nuevo tipo atómico de nombre <nombre>, cuya representación ocupa
<representación> bytes y debe estar alineado a <alineación> bytes.
Por ejemplo: ATOMICO char 1 2 y ATOMICO int 4 4

"""
def atomico(argumentos, memoria):

    # Separamos los argumentos
    nombre = ""
    representacion = ""
    alineacion = ""
    try:
        aux = argumentos.split(' ')
        nombre = aux[0]
        representacion = aux[1]
        alineacion = aux[2]
    except IndexError:
        print("Error en los argumentos recibidos")

    # Definimos el tipo atomico
    if(  nombre in memoria["union"] or nombre in memoria["atomico"] or nombre in memoria["struct"]  ):
        print("El Nombre ya esta definido en memoria\nAccion Ignorada")
    else:
        memoria["atomico"][nombre] = [representacion, alineacion]
    

"""
Se define el registro struct considerando que un registro
puede contener unicamente tipos atomicos
"""
def struct(args, memoria):
    # Separamos los argumentos
    nombre = ""
    tipos = []
    try:
        aux = args.split(' ')
        nombre = aux[0]
        tipos = aux[1:]
    except IndexError:
        print("Error en los argumentos recibidos")

    # Se almacena en memoria el struct
    if(  nombre in memoria["union"] or nombre in memoria["atomico"] or nombre in memoria["struct"] ):
        print("El Nombre ya esta definido en memoria\nAccion Ignorada")
    else:
        memoria["struct"][nombre] = tipos

"""
Se define el registro variable union
"""
def union(args, memoria):
    # Separamos los argumentos
    nombre = ""
    tipos = []
    try:
        aux = args.split(' ')
        nombre = aux[0]
        tipos = aux[1:]
    except IndexError:
        print("Error en los argumentos recibidos")

    # Se almacena en memoria el union
    if( nombre in memoria["union"] or nombre in memoria["atomico"] or nombre in memoria["struct"] ):
        print("El Nombre ya esta definido en memoria\nAccion Ignorada")
    else:
        representacion = maxRepresentacion(tipos,memoria)
        alineacion = mcmAlineacion(tipos, memoria)
        if representacion > -1:
            memoria["union"][nombre] = [representacion, alineacion]


"""
Maxima representacion en lista de tipos atomicos
"""
def maxRepresentacion(tipos, memoria):
    max = -1
    for i in tipos:
        if( not i in memoria["atomico"] ):
            print("Uno de los tipos atomicos en la lista no ha sido definidos")
            max = -1
            break
        max = max( max, int(memoria["atomico"][i][0]) )
    return max


"""
Minimo comun multiplo entre las alineaciones de las representaciones
"""


"""
Ejecuta un bucle recibiendo solicitudes
del usuario
"""
def main():
    """
    La memoria es una lista de diccionarios
    el primer diccionario corresponde a los tipos atomicos
    el segundo a los struct 
    """
    memoria = {
        "atomico": {},
        "struct": {},
        "union": {}
    }

    while(True):
        entrada = input(">> ")
        entrada = entrada.split(" ")
        try:
            tipo = entrada[0]
            argumentos = ""
            if tipo != "SALIR":
                argumentos = " ".join(entrada[1:])
            ejecutar(tipo, argumentos, memoria)
        except IndexError:
            print("Error en el formato de entrada")

"""
Si se llama desde este archivo
se ejecuta la funcion main()
"""

if __name__ == "__main__":
    main()