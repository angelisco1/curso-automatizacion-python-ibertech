import unittest

class Tests(unittest.TestCase):

  @classmethod
  def setUpClass(cls):
    print("Se ejecuta 1 vez al principio del todo")

  def setUp(self):
    print("Se ejecuta justo antes de cada test")

  def test_nums_iguales(self):
    print("Test nums iguales")
    self.assertEqual(2, 2)
    # self.assertEqual(2, 3)

  def test_nums_distintos(self):
    print("Test nums distintos")
    self.assertNotEqual(2, 3)
    # self.assertNotEqual(2, 2)

  def test_numeros_ganadores(self):
    numeros_ganadores = ["12345", "00000", "37928"]
    numero = "12345"
    # numero = "12346"

    self.assertIn(numero, numeros_ganadores)

  def tearDown(self):
    print("Se ejecuta justo después de cada test")

  @classmethod
  def tearDownClass(cls):
    print("Se ejecuta 1 vez al final del todo")


if __name__ == "__main__":
  unittest.main()