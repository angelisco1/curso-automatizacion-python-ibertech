import unittest
import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options


class ApiDemosTest(unittest.TestCase):

    def setUp(self):
        options = UiAutomator2Options()
        options.platform_name = "Android"
        options.automation_name = "UiAutomator2"
        options.device_name = "emulator-5554"
        options.app = "/Users/angelisco1/Pronoide/mis-cursos/curso-ibertech-automatizacion-python/curso-automatizacion-python-ibertech/12-selenium/selenium-webdriver/recursos/ApiDemos-debug.apk"


        self.driver = webdriver.Remote("http://localhost:4723", options=options)
        self.driver.implicitly_wait(10)

    def test_write_in_text_box(self):
        opcion_text = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Text")
        opcion_text.click()

        opcion_log_text_box = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "LogTextBox")
        opcion_log_text_box.click()

        boton_add = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Add")
        boton_add.click()


        # input_text = self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@resource-id='io.appium.android.apis:id/text']")
        input_text = self.driver.find_element(AppiumBy.ID, "io.appium.android.apis:id/text")
        self.assertEqual(input_text.text, "This is a test\n")
        # self.assertEqual(input_text.text, "This is a test")

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
