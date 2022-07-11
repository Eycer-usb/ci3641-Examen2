"""
Programa manejador de tipos de datos
Permite definir tipos atomicos, registros struct
y registros varientes unions
"""

import sys
import math

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
    elif(tipo == "SALIR"):
        sys.exit()
    else:
        print("Orden Incorrecta")

"""
Se define un tipo de dato atomico. Estos 
tipos de datos son los que pueden conformar un
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
    if( nombre in memoria["union"] or nombre in memoria["atomico"] or nombre in memoria["struct"] ):
        print("El Nombre ya esta definido en memoria\nAccion Ignorada")
    else:
        if(not tiposValidos(tipos, memoria)):
            print("Alguno de los tipos atomicos introducidos no estan aun registrados")
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
        if(not tiposValidos(tipos, memoria)):
            print("Alguno de los tipos atomicos introducidos no estan aun registrados")
        else:
            representacion = maxRepresentacion(tipos,memoria)
            alineacion = mcmAlineacion(tipos, memoria)
            if representacion > -1:
                memoria["union"][nombre] = [representacion, alineacion]


"""
Verifica si una lista de datos atomicos es correcta
"""

def tiposValidos(lista, memoria):
    for i in lista:
        if not ( i in memoria['atomico'])    :
            return False
    return True

"""
Se obtiene la representacion mas grande entre los elementos en la lista
"""
def maxRepresentacion(tipos, memoria):
    mx = -1
    for i in tipos:
        mx = max( mx, int(memoria["atomico"][i][0]) )
    return mx


"""
Minimo comun multiplo entre las alineaciones de las representaciones
"""
def mcmAlineacion(tipos, memoria):
    mcm = 1
    for i in tipos:
        a = int(memoria["atomico"][i][1])
        mcm = (mcm*a)//math.gcd(mcm,a)
    return mcm


"""
En caso de solicitarse describir un tipo de dato
se ejecutara la funcion describir. Esta imprimira en
pantalla la información correspondiente al tipo con nombre <nombre>. Se 
incluye, el tamaño, alineación y cantidad de bytes desperdiciados
para el tipo. Se consideran los siguientes casos

• El lenguaje guarda registros y registros viariantes sin empaquetar.
• El lenguaje guarda registros y registros viariantes empaquetados.
• El lenguaje guarda registros y registros viariantes reordenando los campos de
manera óptima (minimizando la memoria, sin violar reglas de alineación).

El programa ignora la acción si <nombre> no corresponde
a algún tipo creado en el programa.
"""
def describir(argumentos, memoria):

    # Separamos los argumentos
    nombre = ""
    try:
        aux = argumentos.split(' ')
        nombre = aux[0]
    except IndexError:
        print("Error en los argumentos recibidos")
    
    if(nombre in memoria["atomico"]):
        describir_tipo_atomico(nombre, memoria)
    elif( nombre in memoria["struct"] ):
        describir_tipo_struct(nombre, memoria)
    elif( nombre in memoria["union"] ):
        describir_tipo_union(nombre, memoria)
    else:
        print("Tipo de dato no Definido")

"""
Dado un dato atomico, este ocupara su representacion de manera optima
sin desperdiciar espacio en memoria. Lo que puede cambiar es la
direccion de memoria donde este almacenado, mas no su tamaño de 
representacion o su alineacion
"""
def describir_tipo_atomico(nombre, memoria):
    print("TIPO ATOMICO")
    print("Tamaño    Alineacion    Bytes desperdiciados")
    print(memoria['atomico'][nombre][0],"\t\t", memoria['atomico'][nombre][0],"\t\t", 0)


"""
Dado un el nombre de un resgitro variante,
en la memoria este ocupara el tamaño del 
elemento que lo pueda conformar mas grande
y su alineacion sera el minimo comun multiplo
de las alineaciones de los posibles tipos
que pueda albergar
"""
def describir_tipo_union( nombre, memoria ):
    print("TIPO UNION")
    print("Tamaño    Alineacion    Bytes desperdiciados")
    print(memoria['union'][nombre][0],"\t\t", memoria['union'][nombre][0],"\t\t", 0)

"""
Dado el nombre de un registro Struct muestra por la salida estandar
los diferentes tamaños posibles del registro y la cantidad de
memoria desperdiciada segun los criterios mencionados anteriormente
"""
def describir_tipo_struct( nombre, memoria ):
    memoria_struct_sin_empaquetar(nombre, memoria)
    memoria_struct_empaquetando(nombre, memoria)
    memoria_struct_reordenando(nombre, memoria)

"""
Espacio en memoria Sin Empaquetar (Respetando Alineaciones)
"""
def memoria_struct_sin_empaquetar(nombre, memoria):
    pass

"""
Espacio en memoria Sin Empaquetar (Respetando Alineaciones)
"""
def memoria_struct_empaquetando(nombre, memoria):
    memoria_ocupada = 0
    atomicos = memoria["struct"][nombre]
    for i in atomicos:
        memoria_ocupada += int(memoria["atomico"][i][0])

    # Suponiendo el tamaño de la palabra igual a 4 bytes
    memoria_desperdiciada = 0
    if (memoria_ocupada %4 != 0):
        memoria_desperdiciada = 4 - memoria_ocupada % 4
    print("TIPO STRUCT CON EMPAQUETADO")
    print("Tamaño    Bytes desperdiciados")
    print(memoria_ocupada," \t\t", memoria_desperdiciada)
    
"""
Espacio en memoria Reordenando de Manera Optima
"""
def memoria_struct_reordenando( nombree, memoria ):
    pass

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