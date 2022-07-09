"""
Se Construye un Evaluador booleano de expresiones
en orden prefijo y posfijo y es capaz de 
traducir una expresion en cualquiera de estos ordenes
a orden infijo natural de cada operador (La negacion se 
establece como prefija en esta traduccion)
"""

import sys

"""
Dada la accion a realizar, la ejecuta
segun los argumentos introducidos por el usuario
"""
def ejecutar(accion, orden, expresion):
    if(accion == "EVAL"):
        evaluar(orden, expresion)
    elif(accion == "MOSTRAR"):
        mostrar(orden, expresion)
    elif(accion == "SALIR"):
        sys.exit()

"""
Al recibir una expresion booleana segun el orden recibido
se retorna la evaluacion de esa expresion booleana
"""
def evaluar(orden, expresion):
    elementos = expresion.split(" ")
    if( orden == "PRE" ):
        print(evaluar_prefijo(elementos))
    elif( orden == "POST" ):
        print(evaluar_posfijo(elementos))

"""
Al recibir una expresion booleana segun el orden indicado
se retorna la expresion booleana reescrita en orden infijo
"""
def mostrar(orden, expresion):
    elementos = expresion.split(" ")
    if( orden == "PRE" ):
        print(prefijo_a_infijo(elementos))
    elif( orden == "POST" ):
        print(posfijo_a_infijo(elementos))

"""
Se recibe expresion booleana en orden prefijo y se traduce a 
orden infijo. La prioridad indica la prioridad de la operacion y el numero_argumento
indica si es el izquierdo o el derecho ( 1 o 2 respectivamente)
"""
def prefijo_a_infijo(elementos, prioridad = 0, numero_argumento = 1) -> str:
    i = 0
    while len(elementos) != 0 :

        if(elementos[i] == "^"):
            del elementos[i]
            sub_exp = prefijo_a_infijo( elementos, 3)
            return "^ " + sub_exp

        elif(elementos[i] == "&" or elementos[i] == "|"):
            op = elementos[i]
            del elementos[i]
            izquierda = prefijo_a_infijo( elementos, 2 )
            derecha = prefijo_a_infijo( elementos, 2 , 2)
            if( 2 < prioridad or ( 2 == prioridad and numero_argumento == 2 )):
                return "(" + izquierda + " " + op + " "+ derecha + ")"
            return izquierda + " " + op + " "+ derecha

        elif(elementos[i] == "=>"):
            del elementos[i]
            izquierda = prefijo_a_infijo( elementos, 1 )
            derecha = prefijo_a_infijo( elementos, 1, 2)
            if(prioridad > 1 or ( prioridad == 1 and numero_argumento == 1 )):
                return "(" + izquierda + " => "+ derecha + ")"
            return izquierda + " => "+ derecha

        elif(elementos[i] == "true" or elementos[i] == "false"):
            aux = elementos[i]
            del elementos[i]
            return aux

"""
Se recibe expresion booleana en orden posfijo y se traduce a 
orden infijo
"""
def posfijo_a_infijo(elementos, prioridad = 0, numero_argumento = 1):
    i = len(elementos) - 1
    while len(elementos) != 0 :

        if(elementos[i] == "^"):
            del elementos[i]
            sub_exp = posfijo_a_infijo( elementos, 3)
            return "^ " + sub_exp

        elif(elementos[i] == "&" or elementos[i] == "|"):
            op = elementos[i]
            del elementos[i]
            derecha = posfijo_a_infijo( elementos, 2 , 2)
            izquierda = posfijo_a_infijo( elementos, 2)
            if( 2 < prioridad or ( 2 == prioridad and numero_argumento == 2 )):
                return "(" + izquierda + " " + op + " "+ derecha + ")"
            return izquierda + " " + op + " "+ derecha

        elif(elementos[i] == "=>"):
            del elementos[i]
            derecha = posfijo_a_infijo( elementos, 1 , 2)
            izquierda = posfijo_a_infijo( elementos, 1)
            if(prioridad > 1 or ( prioridad == 1 and numero_argumento == 1 )):
                return "(" + izquierda + " => "+ derecha + ")"
            return izquierda + " => "+ derecha

        elif(elementos[i] == "true" or elementos[i] == "false"):
            aux = elementos[i]
            del elementos[i]
            return aux
        else:
            del elementos[i]


"""
Se recibe expresion booleana en orden prefijo y se evalua.
La prioridad indica la prioridad de la operacion y el numero_argumento
indica si es el izquierdo o el derecho ( 1 o 2 respectivamente)
"""
def evaluar_prefijo(elementos) -> str:
    i = 0
    while len(elementos) != 0 :

        if(elementos[i] == "^"):
            del elementos[i]
            sub_exp = evaluar_prefijo( elementos)
            return not sub_exp

        elif(elementos[i] == "&" or elementos[i] == "|"):
            op = elementos[i]
            del elementos[i]
            izquierda = evaluar_prefijo( elementos )
            derecha = evaluar_prefijo( elementos)
            if( op == "&" ):
                return izquierda and derecha
            return izquierda or derecha

        elif(elementos[i] == "=>"):
            del elementos[i]
            izquierda = evaluar_prefijo( elementos)
            derecha = evaluar_prefijo( elementos)
            return not izquierda or derecha

        elif(elementos[i] == "true"):
            del elementos[i]
            return True
        elif(elementos[i] == "false"):
            del elementos[i]
            return False


"""
Se recibe expresion booleana en orden prefijo y se evalua.
La prioridad indica la prioridad de la operacion y el numero_argumento
indica si es el izquierdo o el derecho ( 1 o 2 respectivamente)
"""
def evaluar_posfijo(elementos) -> str:
    i = len(elementos) - 1
    while len(elementos) != 0 :

        if(elementos[i] == "^"):
            del elementos[i]
            sub_exp = evaluar_posfijo( elementos )
            return not sub_exp

        elif(elementos[i] == "&" or elementos[i] == "|"):
            op = elementos[i]
            del elementos[i]
            derecha = evaluar_posfijo( elementos )
            izquierda = evaluar_posfijo( elementos )
            if( op == "&" ):
                return izquierda and derecha
            return izquierda or derecha

        elif(elementos[i] == "=>"):
            del elementos[i]
            derecha = evaluar_posfijo( elementos)
            izquierda = evaluar_posfijo( elementos)
            return not izquierda or derecha

        elif(elementos[i] == "true"):
            del elementos[i]
            return True
        elif(elementos[i] == "false"):
            del elementos[i]
            return False

"""
Ejecuta un bucle recibiendo solicitudes
del usuario
"""
def main():
    entrada = input(">> ")
    entrada = entrada.split(" ")
    try:
        accion = entrada[0]
        orden = ""
        expresion = ""
        if accion != "SALIR":
            orden = entrada[1]
            expresion = " ".join(entrada[2:])
        ejecutar(accion, orden, expresion)
    except IndexError:
        print("Error en el formato de entrada")
    main()

"""
Si se llama desde este archivo
se ejecuta la funcion main()
"""

if __name__ == "__main__":
    main()