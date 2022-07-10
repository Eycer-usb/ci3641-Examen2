"""
Segun la definicion dada en el enunciado
y considerando que en mi caso X=2, Y=1 y Z=6
entonces tenemos que alpha = 6 y beta = 5

Por lo tanto la funcion a implementar es:
            
            {  n   si  0 <= n < 30
    F(n) =  {
            {  F(n-5) + F(n-10) + F(n-15) + F(n-20) + ...
            {        ... + F(n-25) + F(n-30)    si n > 30

"""
import sys

# Funcion recursiva basada en la definicion
# Recordamos que alpha = 6 y beta = 5
def F(n) -> int:
    if (0 <= n and n < 30): # 6*5 = 30
        return n
    elif( n >= 30 ):
        ac = 0
        for i in range( 1, 7 ): # recorremos de 1 a alpha
            ac += F( n - i*5 ) # i*beta
        return ac

# Llamador de Funcion Recursiva de cola
def FT(n):

    # Funcion recursiva de cola
    def FT_aux(n : int, arg : list) -> int:

        if (0 <= n and n < 30):
            return arg[-1]

        elif( n >= 30 ):
            # Se obtiene el nuevo argumento
            ac = 0
            for i in arg:
                ac += i
            arg.append(ac)
            del arg[0]
            return FT_aux( n-5, arg )

    # Se obtienen los Argumentos 5 argumentos iniciales
    if( n < 30 ):
        return n
    else:
        a = n%5
        arg = []
        while a < 30:
            arg.append(a)
            a += 5
        
        # Se retorna el resultado obtenido 
        # de la funcion de cola
        return FT_aux(n, arg)

# Funcion iterativa llamadora
def FI(n):

    # Funcion Iterativa
    def FI_aux(n : int, arg : list) -> int:
                                          # Nota:
        while( not (0 <= n and n < 30) ): # Se niega el caso base de la
                                          # Funcion recursiva

            # Se obtiene el nuevo argumento
            ac = 0
            for i in arg:
                ac += i         # Nota
            arg.append(ac)      # el return del caso recursivo se convierte 
            del arg[0]          # en una asignacion, y el decremento de n en 
            n = n - 5           # la llamada recursiva se transforma en
                                # un decremento mediante una asignacion

                       # Nota:
        return arg[-1] # Es el equivalente al return del caso base
                       # de la funcion decursiva 


    # Se obtienen los Argumentos 5 argumentos iniciales
    if( n < 30 ):
        return n
    else:
        a = n%5
        arg = []
        while a < 30:
            arg.append(a)
            a += 5
        
        # Se retorna el resultado obtenido 
        # de la funcion de cola
        return FI_aux(n, arg)

# Script de Demostracion
def main():
    n = int(input("Ingrese el numero a calcular F6,5\n>> "))
    # Que tristeza que python no optimice las 
    # recursiones de cola :')
    print( F(n) )
    print( FT(n) )
    print( FI(n) )


# Ejecutamos un script de demostracion
if __name__ == '__main__':
    
    main()