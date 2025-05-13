import unittest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
import time
import csv
from ddt import ddt, unpack, data

def get_datos_csv(csv_path):
  filas = []
  with open(csv_path, "r") as file:
    reader = csv.reader(file, delimiter=";")
    next(reader)
    for fila in reader:
      filas.append(fila)

  return filas

@ddt
class TestsChrome(unittest.TestCase):

  @classmethod
  def setUpClass(cls):
    options = Options()
    service = Service(executable_path="../../drivers/geckodriver/geckodriver")
    cls.driver = webdriver.Firefox(options=options, service=service)

  def setUp(self):
    self.driver.get("https://auth.wikimedia.org/eswiki/w/index.php?title=Especial:Crear_una_cuenta&returnto=Main_Page&centralauthLoginToken=a8dbfa132efd87b54a5049cad1eaaa94&usesul3=1&useformat=desktop")

  @data(*get_datos_csv("../../recursos/datos-registro.csv"))
  @unpack
  def test_suma(self, usuario, password, confirm_password, email, captcha, error):
    self.driver.find_element(By.NAME, "wpName").send_keys(usuario)
    self.driver.find_element(By.NAME, "wpPassword").send_keys(password)
    self.driver.find_element(By.NAME, "retype").send_keys(confirm_password)
    self.driver.find_element(By.NAME, "email").send_keys(email)
    self.driver.find_element(By.NAME, "captchaWord").send_keys(captcha)

    self.driver.find_element(By.NAME, "wpCreateaccount").click()

    caja_error = self.driver.find_element(By.CLASS_NAME, "cdx-message__content")
    self.assertEqual(caja_error.text, error)


  @classmethod
  def tearDownClass(cls):
    cls.driver.quit()


if __name__ == "__main__":
  unittest.main()