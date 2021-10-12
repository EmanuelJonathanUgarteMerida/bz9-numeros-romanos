import unittest
from romanos import convertir_a_numero


class RomanosTest(unittest.TestCase):
    def test_unidades(self):
        self.assertEqual(convertir_a_numero('I'),1)

    def test_numeros(self):
        self.assertEqual(convertir_a_numero('MCXXIII'),1123)
        self.assertEqual(convertir_a_numero('IV'),4)

if __name__ == '__main__':
    unittest.main()
