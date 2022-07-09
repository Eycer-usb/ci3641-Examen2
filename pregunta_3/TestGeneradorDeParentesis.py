import unittest
from GeneradorDeParentesis import *

class TestGeneradorDeParentesis( unittest.TestCase ):
    def test_caso_base(self):
        for i in parentesis(0):
            self.assertTrue(i == "")
    def test_un_par(self):
        for i in parentesis(1):
            self.assertTrue( i == "()" )
    def test_dos_pares(self):
        resultados = [ "()()", "(())" ]
        cantidad = 0
        for i in parentesis(2):
            self.assertTrue( i in resultados )
            cantidad += 1
        self.assertTrue( cantidad == 2 )
    def test_tres_pares(self):
        resultados = [ "()()()", "((()))", "(())()", "(()())", "()(())" ]
        cantidad = 0
        for i in parentesis(3):
            self.assertTrue( i in resultados )
            cantidad += 1
        self.assertTrue( cantidad == 5 )
    
    def test_cuatro_pares(self):
        resultados = [ "()()()()", "()()(())", "()(())()",
         "(())()()", "()((()))", "((()))()", "()(()())", "(()())()",
         "(())(())", "(((())))", "((()()))", "(()(()))", "((())())", "(()()())" ]
        cantidad = 0
        for i in parentesis(4):
            self.assertTrue( i in resultados )
            cantidad += 1
        self.assertTrue( cantidad == 14 )

if __name__ == "__main__":
    unittest.main()