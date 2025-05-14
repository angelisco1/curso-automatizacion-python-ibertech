import unittest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from libro import Libro
import time

def get_puntuacion_from_class(clases):
  if "One" in clases:
    return 1
  elif "Two" in clases:
    return 2
  elif "Three" in clases:
    return 3
  elif "Four" in clases:
    return 4
  elif "Five" in clases:
    return 5
  else:
    return 0

def get_libros_of_page():
  libros = []

  contenedores_libros = driver.find_elements(By.CSS_SELECTOR, "article.product_pod")

  for contenedor_libro in contenedores_libros:

    titulo = contenedor_libro.find_element(By.CSS_SELECTOR, "h3 > a").get_attribute("title")
    precio = contenedor_libro.find_element(By.CSS_SELECTOR, "p.price_color").text
    imagen_url = contenedor_libro.find_element(By.TAG_NAME, "img").get_attribute("src")
    print(f'----- {contenedor_libro.find_element(By.CLASS_NAME, "star-rating").get_attribute("class")}')
    puntuacion = get_puntuacion_from_class(contenedor_libro.find_element(By.CLASS_NAME, "star-rating").get_attribute("class"))

    libro = Libro(titulo, imagen_url, precio, puntuacion)
    print(libro)
    libros.append(libro)

  return libros


if __name__ == "__main__":


  options = Options()
  service = Service(executable_path="/Users/angelisco1/Pronoide/mis-cursos/curso-ibertech-automatizacion-python/curso-automatizacion-python-ibertech/12-selenium/selenium-webdriver/drivers/geckodriver/geckodriver")
  driver = webdriver.Firefox(options=options, service=service)

  driver.get("https://books.toscrape.com/")

  libros = []

  while True:

    libros_pagina_actual = get_libros_of_page()
    # libros.extend(libros_pagina_actual)
    libros = [*libros, *libros_pagina_actual]

    try:
      boton_siguiente = driver.find_element(By.LINK_TEXT, "next")
      boton_siguiente.click()

    except NoSuchElementException:
      break


  driver.quit()

  print(len(libros))
  for libro in libros:
    print(f"> {libro}")
