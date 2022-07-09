"""
Pruebas unitarias para el Evaluador Booleano

"""

import unittest
from EvaluadorBooleano import *

"""
Pruebas de la funcion prefijo_a_infijo
"""
class TestEvaluadorBooleano_prefijo_a_infijo( unittest.TestCase ):

    def test_minimas_expresiones( self ):
        self.assertTrue( prefijo_a_infijo(["true"]) == "true" )
        self.assertTrue( prefijo_a_infijo(["false"]) == "false" )

    def test_negacion_simple(self):
        self.assertTrue( prefijo_a_infijo(["^", "true"]) == "^ true" )
        self.assertTrue( prefijo_a_infijo(["^", "false"]) == "^ false" )
        self.assertTrue( prefijo_a_infijo(["^", "^", "false"]) == "^ ^ false" )
        self.assertTrue( prefijo_a_infijo(["^", "^", "true"]) == "^ ^ true" )

    def test_conjuncion_disyuncion_simple(self):
        self.assertTrue( prefijo_a_infijo( ["&", "true", "true"] ) == "true & true" )
        self.assertTrue( prefijo_a_infijo( ["&", "false", "true"] ) == "false & true" )
        self.assertTrue( prefijo_a_infijo( ["&", "false", "true"] ) == "false & true" )
        self.assertTrue( prefijo_a_infijo( ["&", "|", "false", "true", "false"] ) == "false | true & false" )
        self.assertTrue( prefijo_a_infijo( ["|", "&", "true", "false", "false"] ) == "true & false | false" )

    def test_implicacion_simple(self):
        self.assertTrue( prefijo_a_infijo( [ "=>", "true", "false" ] ) == "true => false" )
        self.assertTrue( prefijo_a_infijo( [ "=>", "=>", "true", "false", "false" ] ) == "(true => false) => false" )
        self.assertTrue( prefijo_a_infijo( [ "=>", "=>", "=>", "true", "false", "true", "false" ] ) == "((true => false) => true) => false" )

    def test_negacion_conjuncion_disyuncion(self):
        self.assertTrue( prefijo_a_infijo( [ "^", "&", "true", "false" ] ) == "^ (true & false)")
        self.assertTrue( prefijo_a_infijo( [ "^", "|", "true", "false" ] ) == "^ (true | false)")
        self.assertTrue( prefijo_a_infijo( [ "&", "true", "|","^", "false", "true" ] ) == "true & (^ false | true)")
        self.assertTrue( prefijo_a_infijo( [ "^", "&" ,"|", "^", "true", "false", "|","^", "false", "true" ] ) == "^ (^ true | false & (^ false | true))" )

    def test_implicacion_conjuncion_disjuncion(self):
        self.assertTrue( prefijo_a_infijo( [ "=>", "&", "true", "false", "|", "true", "=>", "false", "=>", "true", "false" ] ) == "true & false => true | (false => true => false)" )
    
    def test_tutti(self):
        self.assertTrue( prefijo_a_infijo( [ "=>", "&", "=>", "true", "false", "false", "|", "|", "true", "&", "false", "false", "^", "true" ] ) == \
                                            "(true => false) & false => true | (false & false) | ^ true")

"""
Pruebas de la funcion posfijo_a_infijo
"""
class TestEvaluadorBooleano_posfijo_a_infijo( unittest.TestCase ):
    def test_minimas_expresiones( self ):
        self.assertTrue( posfijo_a_infijo(["true"]) == "true" )
        self.assertTrue( posfijo_a_infijo(["false"]) == "false" )

    def test_negacion_simple(self):
        self.assertTrue( posfijo_a_infijo(["true", "^"]) == "^ true" )
        self.assertTrue( posfijo_a_infijo(["false", "^"]) == "^ false" )
        self.assertTrue( posfijo_a_infijo([ "false", "^", "^"]) == "^ ^ false" )
        self.assertTrue( posfijo_a_infijo(["true", "^", "^"]) == "^ ^ true" )

    def test_conjuncion_disyuncion_simple(self):
        self.assertTrue( posfijo_a_infijo( ["true", "true", "&"] ) == "true & true" )
        self.assertTrue( posfijo_a_infijo( [ "false", "true", "&"] ) == "false & true" )
        self.assertTrue( posfijo_a_infijo( [ "true", "false", "&"] ) == "true & false" )
        self.assertTrue( posfijo_a_infijo( [ "false", "true", "|", "false", "&"] ) == "false | true & false" )
        self.assertTrue( posfijo_a_infijo( ["true", "false","&", "false", "|"] ) == "true & false | false" )

    def test_implicacion_simple(self):
        self.assertTrue( posfijo_a_infijo( [ "true", "false", "=>" ] ) == "true => false" )
        self.assertTrue( posfijo_a_infijo( [ "true", "false", "=>", "false", "=>" ] ) == "(true => false) => false" )
        self.assertTrue( posfijo_a_infijo( [ "true", "false", "=>", "true", "=>", "false", "=>" ] ) == "((true => false) => true) => false" )

    def test_negacion_conjuncion_disyuncion(self):
        self.assertTrue( posfijo_a_infijo( [ "true", "false", "&", "^" ] ) == "^ (true & false)")
        self.assertTrue( posfijo_a_infijo( ["true", "false", "|", "^" ] ) == "^ (true | false)")
        self.assertTrue( posfijo_a_infijo( [ "true", "false","^", "true", "|", "&" ] ) == "true & (^ false | true)")
        self.assertTrue( posfijo_a_infijo( [ "true", "^", "false","|","false","^","true","|", "&", "^"] ) == "^ (^ true | false & (^ false | true))" )

    def test_implicacion_conjuncion_disjuncion(self):
        self.assertTrue( posfijo_a_infijo( [ "true", "false", "&", "true", "false", "true", "false", "=>", "=>", "|", "=>" ] ) == "true & false => true | (false => true => false)" )
    
    def test_tutti(self):
        self.assertTrue( posfijo_a_infijo( ["true", "false", "=>", "false", "&", "true", "false", "false", "&", "|", "true", "^", "|", "=>"] ) == \
                                            "(true => false) & false => true | (false & false) | ^ true")
        self.assertTrue( posfijo_a_infijo( [ "true", "false", "=>", "false", "|", "true", "false", "^", "|", "&" ] ) == \
                                            "(true => false) | false & (true | ^ false)" )

"""
Pruebas de la funcion evaluador_prefijo
"""
class TestEvaluadorBooleano_evaluador_prefijo( unittest.TestCase ):

    def test_minimos(self):
        self.assertTrue( evaluar_prefijo( [ "true" ] ) == True)
        self.assertTrue( evaluar_prefijo( [ "false" ] ) == False)

    def test_simples(self):
        self.assertTrue( evaluar_prefijo( ["^", "true"] ) == False)
        self.assertTrue( evaluar_prefijo( [ "^", "false"] ) == True)
        self.assertTrue( evaluar_prefijo( [  "^", "^", "false"]) == False ) 
        self.assertTrue( evaluar_prefijo( [ "^", "^", "true"]) == True )

    def test_conjuncion_disyuncion_simple(self):
        self.assertTrue( evaluar_prefijo( ["&", "true", "true"] ) == True )
        self.assertTrue( evaluar_prefijo( ["&", "false", "true"] ) == False )
        self.assertTrue( evaluar_prefijo( ["&", "true", "false"] ) == False )
        self.assertTrue( evaluar_prefijo( ["&", "|", "false", "true", "false"] ) == False)
        self.assertTrue( evaluar_prefijo( ["|", "&", "true", "false", "false"] ) == False )

    def test_implicacion_simple(self):
        self.assertTrue( evaluar_prefijo( [ "=>", "true", "false" ] ) == False )
        self.assertTrue( evaluar_prefijo( [ "=>", "=>", "true", "false", "false" ] ) == True )
        self.assertTrue( evaluar_prefijo( [ "=>", "=>", "=>", "true", "false", "true", "false" ] ) == False )

    def test_negacion_conjuncion_disyuncion(self):
        self.assertTrue( evaluar_prefijo( [ "^", "&", "true", "false" ] ) == True)
        self.assertTrue( evaluar_prefijo( [ "^", "|", "true", "false" ] ) == False)
        self.assertTrue( evaluar_prefijo( [ "&", "true", "|","^", "false", "true" ] ) == True)
        self.assertTrue( evaluar_prefijo( [ "^", "&" ,"|", "^", "true", "false", "|","^", "false", "true" ] ) == True )

    def test_implicacion_conjuncion_disjuncion(self):
        self.assertTrue( evaluar_prefijo( [ "=>", "&", "true", "false", "|", "true", "=>", "false", "=>", "true", "false" ] ) == True )
    
    def test_tutti(self):
        self.assertTrue( evaluar_prefijo( [ "=>", "&", "=>", "true", "false", "false", "|", "|", "true", "&", "false", "false", "^", "true" ] ) == True)

"""
Pruebas de la funcion evaluador_posfijo
"""
class TestEvaluadorBooleano_evaluador_posfijo( unittest.TestCase ):

    def test_minimos(self):
        self.assertTrue( evaluar_posfijo( [ "true" ] ) == True)
        self.assertTrue( evaluar_posfijo( [ "false" ] ) == False)

    def test_simples(self):
        self.assertTrue( evaluar_posfijo( ["true", "^"] ) == False)
        self.assertTrue( evaluar_posfijo( ["false", "^"] ) == True)
        self.assertTrue( evaluar_posfijo( [ "false", "^", "^"] ) == False ) 
        self.assertTrue( evaluar_posfijo( ["true", "^", "^"] ) == True )

    def test_conjuncion_disyuncion_simple(self):
        self.assertTrue( evaluar_posfijo( ["true", "true", "&"] ) == True )
        self.assertTrue( evaluar_posfijo( [ "false", "true", "&"] ) == False )
        self.assertTrue( evaluar_posfijo( [ "true", "false", "&"] ) == False )
        self.assertTrue( evaluar_posfijo( [ "false", "true", "|", "false", "&"] ) == False)
        self.assertTrue( evaluar_posfijo( ["true", "false","&", "false", "|"] ) == False )

    def test_implicacion_simple(self):
        self.assertTrue( evaluar_posfijo( [ "true", "false", "=>" ] ) == False )
        self.assertTrue( evaluar_posfijo( [ "true", "false", "=>", "false", "=>" ] ) == True )
        self.assertTrue( evaluar_posfijo( [ "true", "false", "=>", "true", "=>", "false", "=>" ] ) == False )

    def test_negacion_conjuncion_disyuncion(self):
        self.assertTrue( evaluar_posfijo( [ "true", "false", "&", "^" ] ) == True)
        self.assertTrue( evaluar_posfijo( ["true", "false", "|", "^" ] ) == False)
        self.assertTrue( evaluar_posfijo( [ "true", "false","^", "true", "|", "&" ] ) == True)
        self.assertTrue( evaluar_posfijo( [ "true", "^", "false","|","false","^","true","|", "&", "^"] ) == True )

    def test_implicacion_conjuncion_disjuncion(self):
        self.assertTrue( evaluar_posfijo( [ "true", "false", "&", "true", "false", "true", "false", "=>", "=>", "|", "=>" ] ) == True )
    
    def test_tutti(self):
        self.assertTrue( evaluar_posfijo( ["true", "false", "=>", "false", "&", "true", "false", "false", "&", "|", "true", "^", "|", "=>"] ) == True)
        self.assertTrue( evaluar_posfijo( [ "true", "false", "=>", "false", "|", "true", "false", "^", "|", "&" ] ) == False)


# Ejecutamos las pruebas si es invocado
if __name__ == "__main__":
    unittest.main()