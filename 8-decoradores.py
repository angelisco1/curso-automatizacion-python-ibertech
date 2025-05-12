import time

def log(func):

  def wrapper(*args, **kwargs):
    print(f"Estás llamando a la función {func.__name__} con los parámetros {args}")
    resultado = func(*args)
    print(f"El resultado es: {resultado}")
    return resultado

  return wrapper


@log
def suma(num1, num2):
  return num1 + num2


# Es la función wrapper del decorador
print(suma(1, 2))


def measure_time(function):

  def wrapper(*args, **kwargs): # Indicamos el tipo de argumentos que espera wrapper
    import time #Importamos el módulo "time"
    start = time.time() #Establecemos el tiempo de inicio
    result = function(*args, **kwargs) #asociamos la función a una variable
    total = time.time() - start # Calcualmos el tiempo de ejecución
    print(total, 'seconds')
    return result

  return wrapper

# @measure_time #Aplicamos el decorador
# def suma(a, b):
#   time.sleep(3)
#   return a + b
# print(suma(10, 20))

@measure_time #Aplicamos el decorador
def suma2(a, b):
  return a + b
print(suma2(10, 20))