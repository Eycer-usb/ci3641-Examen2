"""
Generador de parentesis contiene un
iterador verdadero nombrado parentesis que dado un 
numero natural permite iterar sobre los posibles valores
formados con esa cantidad de pares de parentesis
garantizando que ese orden de parentizado sea correcto

"""
import sys
def parentesis(n):
    if n == 0:
        yield ""
    else:
        # Memoria para evitar repetidos
        memoria = set()
        for elem in parentesis(n-1):  # Llamada recursiva
            # Ventanas deslizantes
            for i in range(0,2*n):
                for j in range(i+1, 2*n):

                    # Creamos una lista de tamaño 2n 
                    # inicializada con None
                    respuesta_posible = [None] * 2*n
                    respuesta_posible[i] = '('
                    respuesta_posible[j] = ')'

                    # Llenamos el resto de la lista
                    indice = 0
                    for k in range(len(respuesta_posible)):
                        if respuesta_posible[k] == None:
                            respuesta_posible[k] = elem[indice]
                            indice += 1

                    # Si no se ha retornado antes la posible distribucion
                    # obtenida, se retorna y al llamador y se
                    # continua con el calculo del siguiente elemento
                    respuesta_posible = "".join(respuesta_posible)
                    if (not (respuesta_posible in memoria) ):
                        memoria.add(respuesta_posible)
                        yield respuesta_posible
                
                 

"""
Funcion Llamadora del iterador parentesis
"""
def main():
    n = int(input("Introduzca la cantidad de pares de parentesis: \n>> "))
    for i in parentesis(n):
        print( i )

"""
Cuando es ejecutado desde este archivo invoca a la funcion llamadora
"""
if __name__ == '__main__':
    sys.setrecursionlimit(5000)
    main()