import abc
from unittest import TestCase, main, result
import AC02

class Testes(TestCase):

    def test_soma1(self):
        calculador = AC02.Calculadora()
        result = calculador.calcular(4,5,'soma')
        self.assertEqual(result,9)

    def test_soma2(self):
        calculador = AC02.Calculadora()
        result = calculador.calcular(4,5,'+')
        self.assertEqual(result,9)

    def test_multiplicacao1(self):
        calculador = AC02.Calculadora()
        result = calculador.calcular(2,4,'multiplicacao')
        self.assertEqual(result,8)

    def test_multiplicacao2(self):
        calculador = AC02.Calculadora()
        result = calculador.calcular(2,4,'*')
        self.assertEqual(result,8)

    def test_divisao1(self):
        calculador = AC02.Calculadora()
        result = calculador.calcular(10,5,'divisao')
        self.assertEqual(result,2)

    def test_divisao2(self):
        calculador = AC02.Calculadora()
        result = calculador.calcular(10,5,'/')
        self.assertEqual(result,2)

    def test_subtracao1(self):
        calculador = AC02.Calculadora()
        result = calculador.calcular(10,3,'subtracao')
        self.assertEqual(result,7)

    def test_subtracao2(self):
        calculador = AC02.Calculadora()
        result = calculador.calcular(10,3,'-')
        self.assertEqual(result,7)

    def test_erro(self):
        calculador = AC02.Calculadora()
        result = calculador.calcular(10,3,'erro')
        self.assertEqual(result,0)

if __name__ == '__main__':
    main()