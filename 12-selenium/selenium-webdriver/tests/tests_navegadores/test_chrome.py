import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time

class TestsChrome(unittest.TestCase):

  @classmethod
  def setUpClass(cls):
    options = Options()
    service = Service(executable_path="../../drivers/chromedriver/chromedriver")
    cls.driver = webdriver.Chrome(options=options, service=service)

  def setUp(self):
    self.driver.get("http://google.com")

  def test_chrome(self):
    time.sleep(3)

  @classmethod
  def tearDownClass(cls):
    cls.driver.quit()


if __name__ == "__main__":
  unittest.main()