"""
Suite de Pruebas del Manejador de Tipos de Datos
"""

import unittest as ut
from ManejadorDeTipos import *

class TestManejadorDeTipos( ut.TestCase ):

    #Definir Tipos Atomicos
    def test_tipos_atomicos(self):
        memoria = {
        "atomico": {},
        "struct": {},
        "union": {}
        }
        ejecutar("ATOMICO", "int 4 4", memoria)
        self.assertTrue( tiposValidos(["int"], memoria) )
        self.assertTrue( memoria["atomico"]["int"][0] == "4" )
        self.assertTrue( memoria["atomico"]["int"][1] == "4" )
    # Definir Tipos Struct
    def test_tipos_struct(self):
        memoria = {
            "atomico": {},
            "struct": {},
            "union": {}
        }
        ejecutar("ATOMICO", "int 4 4", memoria)
        ejecutar("ATOMICO", "char 4 4", memoria)
        ejecutar("STRUCT", "test int char", memoria)
        self.assertTrue("test" in memoria["struct"])
        self.assertTrue("int" in memoria["struct"]["test"])
        self.assertTrue("char" in memoria["struct"]["test"])

    # Definir Tipos Union
    def test_tipos_union(self):
        memoria = {
            "atomico": {},
            "struct": {},
            "union": {}
        }
        ejecutar("ATOMICO", "int 4 4", memoria)
        ejecutar("ATOMICO", "char 8 3", memoria)
        ejecutar("ATOMICO", "float 10 5", memoria)

        ejecutar("UNION", "test int char float", memoria)
        self.assertTrue("test" in memoria["union"])
        self.assertTrue( memoria['union']['test'][0] == 10 )
        self.assertTrue( memoria['union']['test'][1] == 60 )





if __name__ == "__main__":
    ut.main()