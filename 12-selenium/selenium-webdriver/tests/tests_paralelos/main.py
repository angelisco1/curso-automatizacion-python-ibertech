import concurrent.futures
from test_desplegables import TestsDesplegables

def ejecutar_en_paralelo():
  test_case = TestsDesplegables()

  test_methods = [test_case.test_desplegables_firefox, test_case.test_desplegables_chrome]

  with concurrent.futures.ThreadPoolExecutor(max_workers=len(test_methods)) as executor:

    resultado_de_tests = list(executor.map(lambda test: test(), test_methods))
    # Devuelve True si todas los valores en el iterable son True
    if all(resultado_de_tests):
      print("Todas las pruebas se han ejecutado correctamente.")
    else:
      print("Alguna prueba ha fallado.")

    return all(resultado_de_tests)


if __name__ == '__main__':
  ejecutar_en_paralelo()