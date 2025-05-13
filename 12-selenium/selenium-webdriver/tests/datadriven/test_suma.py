import unittest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
import time
from ddt import ddt, unpack, data

@ddt
class TestsChrome(unittest.TestCase):

  @classmethod
  def setUpClass(cls):
    options = Options()
    service = Service(executable_path="../../drivers/geckodriver/geckodriver")
    cls.driver = webdriver.Firefox(options=options, service=service)

  def setUp(self):
    self.driver.get("http://google.com")

  @data([1, 2, 3], [7, 3, 10], [0, 0, 0])
  @unpack
  def test_suma(self, num1, num2, resultado):
    suma = num1 + num2
    self.assertEqual(suma, resultado)

  @classmethod
  def tearDownClass(cls):
    cls.driver.quit()


if __name__ == "__main__":
  unittest.main()