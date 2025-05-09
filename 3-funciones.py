def suma(n1, n2):
  # pass
  return n1 + n2


suma_nums = suma(1, 2)
print(suma_nums)

def saludar(nombre='Mundo'):
  print(f"Hola {nombre}")

saludar('Ángel')
saludar()


# *args y **kwargs

def get_ticket_loteria(sorteo, *args):
  # print(type(args))
  lista_nums = []
  for num in args:
    lista_nums.append(str(num))

  return f"Tus números para el sorteo {sorteo} son: {', '.join(lista_nums)}"

primitiva = get_ticket_loteria("primitiva", 4, 13, 24, 28, 35, 41)
print(primitiva)

bonoloto = get_ticket_loteria("bonoloto", 4, 13, 24, 28, 35)
print(bonoloto)



persona1 = {
  "nombre": "Charly Falco",
  "edad": 42,
  "esta_trabajando": True
}

persona2 = {
  "nombre": "Json Statham",
  "edad": 53,
  "esta_trabajando": False
}

persona3 = {
  "nombre": "Octavia Blake",
  "edad": 43,
  "esta_trabajando": True
}

def filtrar_personas(lista_personas, **kwargs):
  print(kwargs)
  resultado = []

  for persona in lista_personas:
    condiciones_cumplidas = 0

    if "esta_trabajando" in kwargs.keys() and kwargs["esta_trabajando"] == persona["esta_trabajando"]:
      condiciones_cumplidas += 1

    if "edad_mayor" in kwargs.keys() and persona["edad"] > kwargs["edad_mayor"]:
      condiciones_cumplidas += 1

    if condiciones_cumplidas == len(kwargs.keys()):
      resultado.append(persona)

  return resultado

personas_trabajando_mayores_de_50 = filtrar_personas([persona1, persona2, persona3], esta_trabajando=True, edad_mayor=50)
print(personas_trabajando_mayores_de_50)

personas_trabajando = filtrar_personas([persona1, persona2, persona3], esta_trabajando=True)
print(personas_trabajando)


# def add_elemento_a_lista(elemento, lista=[]):
#   lista.append(elemento)
#   return lista


def add_elemento_a_lista(elemento, lista=None):
  if not lista:
    lista = []
  lista.append(elemento)
  return lista


print(add_elemento_a_lista(1, [0, 2]))
print(add_elemento_a_lista(10, [0, 2, 9]))
print(add_elemento_a_lista(10))
print(add_elemento_a_lista(13))