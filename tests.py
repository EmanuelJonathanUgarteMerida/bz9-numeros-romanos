import unittest
from romanos import convertir_a_numero


class RomanosTest(unittest.TestCase):

    def test_no_resta_multiplo_cinco(self):
        with self.assertRaises(ValueError):
            convertir_a_numero("VX")
            convertir_a_numero("VC")
            convertir_a_numero("VD")
            convertir_a_numero("VM")

            convertir_a_numero("LC")
            convertir_a_numero("LD")
            convertir_a_numero("LM")
            convertir_a_numero("DM")

    def test_no_repetir_cincos(self):
        with self.assertRaises(ValueError):
            convertir_a_numero("VVF")

    def test_no_mas_de_tres_repeticiones(self):
        with self.assertRaises(ValueError):
            convertir_a_numero("IIII")


if __name__ == '__main__':
    unittest.main()
