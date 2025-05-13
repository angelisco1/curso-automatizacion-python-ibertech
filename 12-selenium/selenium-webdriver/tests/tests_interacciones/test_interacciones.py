import unittest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class TestsMetodosDeBusqueda(unittest.TestCase):

  @classmethod
  def setUpClass(cls):
    options = Options()
    service = Service(executable_path="../../drivers/geckodriver/geckodriver")
    cls.driver = webdriver.Firefox(options=options, service=service)

  # def setUp(self):
  #   time.sleep(1.5)

  # def test_documentacion_selenium(self):
  #   self.driver.get("http://google.com")

  #   boton_cookies = self.driver.find_element(By.CSS_SELECTOR, "#W0wltc")
  #   boton_cookies.click()

  #   input = self.driver.find_element(By.NAME, "q")
  #   input.send_keys("selenium")
  #   input.submit()

  #   time.sleep(15)

  #   link_selenium = self.driver.find_element(By.CLASS_NAME, "LC20lb")
  #   print(f"link_selenium text: {link_selenium.text}")
  #   # link_selenium = self.driver.find_element(By.LINK_TEXT, "Selenium")
  #   link_selenium.click()
  #   # time.sleep(2)

  #   titulo = self.driver.find_element(By.TAG_NAME, "h1")
  #   self.assertEqual(titulo.text, "Selenium automates browsers. That's it!")
  #   # time.sleep(2)

  #   link_documentacion = self.driver.find_element(By.LINK_TEXT, "Documentation")
  #   link_documentacion.click()
  #   # time.sleep(2)

  #   titulo_documentacion = self.driver.find_element(By.CSS_SELECTOR, "div.td-content h1")
  #   self.assertEqual(titulo_documentacion.text, "The Selenium Browser Automation Project")
  #   # time.sleep(2)


  def test_desplegables(self):
    self.driver.get("http://localhost:8080/desplegables.html")

    select_coches = Select(self.driver.find_element(By.ID, "car-options"))
    self.assertEqual(select_coches.first_selected_option.text, "BMW")
    self.assertEqual(len(select_coches.options), 4)

    select_coches.select_by_visible_text("Audi")
    self.assertEqual(select_coches.first_selected_option.text, "Audi")

    select_coches.select_by_index(3)
    self.assertEqual(select_coches.first_selected_option.text, "Mercedes")

    select_coches.select_by_value("tesla")
    self.assertEqual(select_coches.first_selected_option.text, "Tesla")


  def test_desplegables_multiple(self):
    self.driver.get("http://localhost:8080/desplegables.html")

    select_colores = Select(self.driver.find_element(By.ID, "color-options"))
    self.assertEqual(len(select_colores.options), 4)
    self.assertTrue(select_colores.is_multiple)

    select_colores.select_by_visible_text("Red")
    select_colores.select_by_visible_text("Blue")
    self.assertEqual(len(select_colores.all_selected_options), 2)

    select_colores.deselect_by_visible_text("Blue")
    self.assertEqual(len(select_colores.all_selected_options), 1)

    select_colores.deselect_all()
    self.assertEqual(len(select_colores.all_selected_options), 0)

  def test_alerts(self):
    self.driver.get("http://localhost:8080/alerts.html")
    self.driver.find_element(By.ID, "show-alert").click()

    alert = self.driver.switch_to.alert
    self.assertEqual(alert.text, "Has pulsado el botón...")
    alert.accept()

  def test_keys(self):
    self.driver.get("https://todomvc.com/examples/javascript-es6/dist/")
    input = self.driver.find_element(By.CSS_SELECTOR, "header input.new-todo")
    input.send_keys("Ir al gimnasio")
    input.send_keys(Keys.ENTER)

    lista_tareas = self.driver.find_elements(By.CSS_SELECTOR, "ul.todo-list li")
    assert len(lista_tareas) == 1

  def test_doble_click(self):
    self.driver.get("http://localhost:8080/doble-click.html")

    caja = self.driver.find_element(By.ID, "caja-doble-click")
    self.assertEqual(caja.value_of_css_property("background-color"), "rgb(0, 0, 255)")

    action_chains = ActionChains(self.driver)
    time.sleep(2)

    action_chains.double_click(caja).perform()

    time.sleep(2)
    self.assertEqual(caja.value_of_css_property("background-color"), "rgb(255, 255, 0)")

  def test_waits_1(self):
    self.driver.implicitly_wait(4)

    self.driver.get("http://localhost:8080/sincronizacion.html")
    boton = self.driver.find_element(By.ID, "btn")

  def test_waits_2(self):
    self.driver.get("http://localhost:8080/sincronizacion.html")
    self.driver.delete_all_cookies()

    wait = WebDriverWait(self.driver, 5)
    wait.until(EC.presence_of_element_located((By.ID, "btn")))

    boton = self.driver.find_element(By.ID, "btn")


  @classmethod
  def tearDownClass(cls):
    cls.driver.quit()


if __name__ == "__main__":
  unittest.main()