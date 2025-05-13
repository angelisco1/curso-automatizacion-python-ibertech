import unittest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
import time

class TestsChrome(unittest.TestCase):

  @classmethod
  def setUpClass(cls):
    options = Options()
    service = Service(executable_path="../../drivers/geckodriver/geckodriver")
    cls.driver = webdriver.Firefox(options=options, service=service)

  def setUp(self):
    self.driver.get("http://google.com")

  def test_firefox(self):
    time.sleep(3)

  @classmethod
  def tearDownClass(cls):
    cls.driver.quit()


if __name__ == "__main__":
  unittest.main()