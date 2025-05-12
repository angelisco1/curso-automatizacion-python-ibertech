from persona import Persona

def divide(num1, num2):
  try:
    return num1 / num2
  # except ZeroDivisionError:
  #   return None
  # except TypeError:
  #   return None
  except Exception:
    return None
  finally:
    print('Siempre se pasa por aquí')

divide(1, 0)
divide(1, "a")


# Tiene que ser mayor de edad
def asignar_edad(persona, edad):
  if edad >= 18:
    persona.edad = edad
  else:
    raise Exception("Tienes que ser mayor de edad")

charly = Persona("Charly", "Falco", 0, True, "0000000T")
# asignar_edad(charly, 12)
asignar_edad(charly, 22)


# Crear nuestras propias excepciones
class HttpError(Exception):
  def __init__(self, code, message):
    self.code = code
    self.code_text = HttpError.get_code_text_from_code(code)
    self.message = message
    self.name = "HttpError"
    super().__init__(f"Petición con error {self.code} ({self.code_text}): {self.message}")

  @staticmethod
  def get_code_text_from_code(code):
    codigos = {
      400: "Bad Request",
      401: "Unauthorized",
      403: "Forbidden",
      500: "Internal Server Error",
    }
    return codigos[code]


def login(usuario, password):
  credenciales_validas = {
    "usuario": "cfalco",
    "password": "1234"
  }

  if credenciales_validas["usuario"] == usuario and credenciales_validas["password"] == password:
    return "1234567890abc"
  else:
    raise HttpError(401, "Credenciales invalidas")


login("cfalco", "1234")
login("cfalco", "12345")