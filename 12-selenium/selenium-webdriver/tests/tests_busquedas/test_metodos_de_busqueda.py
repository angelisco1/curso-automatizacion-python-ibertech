import unittest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
import time

class TestsMetodosDeBusqueda(unittest.TestCase):

  @classmethod
  def setUpClass(cls):
    options = Options()
    service = Service(executable_path="../../drivers/geckodriver/geckodriver")
    cls.driver = webdriver.Firefox(options=options, service=service)

  def setUp(self):
    # time.sleep(1.5)
    self.driver.get("http://localhost:8080")

  def test_by_id(self):
    input = self.driver.find_element(By.ID, "username")
    self.assertEqual(input.get_attribute("name"), "user")

  def test_by_name(self):
    input = self.driver.find_element(By.NAME, "user")
    self.assertEqual(input.get_attribute("id"), "username")

  def test_by_name2(self):
    form = self.driver.find_element(By.ID, "crear-usuario-form")
    input = form.find_element(By.NAME, "user")
    self.assertEqual(input.get_attribute("id"), "nombre")

  def test_by_class_name(self):
    botones_editar = self.driver.find_elements(By.CLASS_NAME, "btn-editar")
    self.assertEqual(len(botones_editar), 5)

  def test_by_tag_name(self):
    formulario_2 = self.driver.find_element(By.ID, "crear-usuario-form")
    labels_formulario_2 = formulario_2.find_elements(By.TAG_NAME, "label")
    labels = ["Nombre", "Apellidos"]
    for label in labels_formulario_2:
      self.assertIn(label.text, labels)

  def test_by_link_text(self):
    link_logout = self.driver.find_element(By.LINK_TEXT, "Logout")
    self.assertEqual(link_logout.get_attribute("href"), "http://localhost:8080/logout")
    self.assertIn("/logout", link_logout.get_attribute("href"))

  def test_by_partial_link_text(self):
    link_notificaciones = self.driver.find_element(By.PARTIAL_LINK_TEXT, "sin leer")
    self.assertEqual(link_notificaciones.get_attribute("href"), "http://localhost:8080/notificaciones")

  def test_by_xpath(self):
    imagenes_con_alt = self.driver.find_elements(By.XPATH, "//img[@alt]")
    imagenes_sin_alt = self.driver.find_elements(By.XPATH, "//img[not(@alt)]")
    self.assertEqual(len(imagenes_con_alt), 1)
    self.assertEqual(len(imagenes_sin_alt), 1)
    # imagenes_con_alt = self.driver.find_elements(By.XPATH, "//div[@id='imagenes']/img/@alt]")
    # self.assertEqual(len(imagenes_con_alt), 1)
    segundo_link = self.driver.find_element(By.XPATH, "/html/body/header/nav/ul/li[2]/a")
    self.assertEqual(segundo_link.text, "Tienes 15 notificaciones sin leer")

  def test_by_css_selector(self):
    segundo_link = self.driver.find_element(By.CSS_SELECTOR, "html > body > header > nav > ul > li:nth-child(2) > a")
    self.assertEqual(segundo_link.text, "Tienes 15 notificaciones sin leer")

    labels_formulario_2 = self.driver.find_elements(By.CSS_SELECTOR, "#crear-usuario-form label")
    labels = ["Nombre", "Apellidos"]
    for label in labels_formulario_2:
      self.assertIn(label.text, labels)

    botones_desabilitados = self.driver.find_elements(By.CSS_SELECTOR, "button:disabled")
    self.assertEqual(len(botones_desabilitados), 3)

  def test_con_buena_practica(self):
    boton = self.driver.find_element(By.CSS_SELECTOR, "button[data-test='boton-editar-3']")
    self.assertEqual(boton.text, "Editar")


  @classmethod
  def tearDownClass(cls):
    cls.driver.quit()


if __name__ == "__main__":
  unittest.main()