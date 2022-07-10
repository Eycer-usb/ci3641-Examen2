"Suite de Pruebas "

import unittest
from FamiliaFibonacci import *

class Test_FamiliaFibonacci(unittest.TestCase):

    def test_casos_base(self):
        for i in range(30):
            self.assertTrue( F(i) == i )
            self.assertTrue( FT(i) == i )
            self.assertTrue( FI(i) == i )

    def test_casos_definidos(self):
        self.assertTrue( F(30) == 75 )
        self.assertTrue( FT(30) == 75 )
        self.assertTrue( FI(30) == 75 )
        self.assertTrue( F(35) == 150 )
        self.assertTrue( FT(35) == 150 )
        self.assertTrue( FI(35) == 150 )
        self.assertTrue( F(43) == 358 )
        self.assertTrue( FT(43) == 358 )
        self.assertTrue( FI(43) == 358 )
        
    def test_igualdad( self ):
        for i in range(30,120):
            self.assertTrue( F(i) == FI(i) == FT(i) )

if __name__ == '__main__':
    unittest.main()