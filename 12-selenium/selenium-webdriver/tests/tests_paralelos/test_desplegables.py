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

class TestsDesplegables(unittest.TestCase):

  def test_desplegables_firefox(self):
    firefox_options = webdriver.FirefoxOptions()
    driver = webdriver.Remote(command_executor="http://192.168.0.21:4444/wd/hub", options=firefox_options)
    self._ejecutar_test_desplegables(driver)
    driver.quit()

  def test_desplegables_chrome(self):
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Remote(command_executor="http://192.168.0.21:4444/wd/hub", options=chrome_options)
    self._ejecutar_test_desplegables(driver)
    driver.quit()


  def _ejecutar_test_desplegables(self, driver):
    driver.get("http://localhost:8080/desplegables.html")

    select_coches = Select(driver.find_element(By.ID, "car-options"))
    self.assertEqual(select_coches.first_selected_option.text, "BMW")
    self.assertEqual(len(select_coches.options), 4)

    time.sleep(5)

    select_coches.select_by_visible_text("Audi")
    self.assertEqual(select_coches.first_selected_option.text, "Audi")

    select_coches.select_by_index(3)
    self.assertEqual(select_coches.first_selected_option.text, "Mercedes")

    select_coches.select_by_value("tesla")
    self.assertEqual(select_coches.first_selected_option.text, "Tesla")


if __name__ == "__main__":
  unittest.main()