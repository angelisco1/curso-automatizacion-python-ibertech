# String
texto = "Hola mundo"
print(texto)

# Int
cantidad = 12

# Float
precio = 2.95

print(type(cantidad))
print(type(precio))

# Boolean
hay_stock = False

# None
es_null = None

print(int(precio))
print(round(precio))


# Formateadores
producto = "Post its"
producto_en_almacen = 20
producto_en_almacen = producto_en_almacen - cantidad
hay_stock = producto_en_almacen - cantidad > 0
total_compra = cantidad * precio

print(producto + ": stock (" + str(producto_en_almacen) + "), ultima compra (" + str(cantidad) + ")")
print("%s: stock (%d), ultima compra (%d)" % (producto, producto_en_almacen, cantidad))

# Nuevo formateador
print("{}: stock ({}), ultima compra ({})".format(producto, producto_en_almacen, cantidad))

# f-string
print(f"{producto}: stock ({producto_en_almacen}), ultima compra ({cantidad})")


# Lista
lista_de_datos = ["un texto", 1, False, [1, 2, 3], None]
lista_productos = [producto, "Clips", "Grapadora", "Calculadora"]

print(lista_productos)
print(len(lista_productos))
print(len(producto))

print(lista_productos[3])

lista_productos.append("Bolis")
print(lista_productos)

bolis = lista_productos.pop()
print(bolis)
print(lista_productos)

lista_productos.clear()
print(lista_productos)

lista_productos_2 = ["Post its", "Clips", "Grapadora", "Calculadora"]
print(lista_productos == lista_productos_2)
lista_productos_2[0] = "Post-its"
print(lista_productos_2)


# Diccionarios
persona = {
  "nombre": "Charly",
  "apellido": "Falco",
  "edad": 42
}

print(f"{persona['nombre']} {persona['apellido']} tiene {persona['edad']} años")
persona["edad"] += 1
print(f"{persona['nombre']} {persona['apellido']} tiene {persona['edad']} años")

print(persona.keys())
print(persona.values())


# Slicing
lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

ultimo_numero = lista_numeros[-1]
print(ultimo_numero)

lista_numeros_del_2_al_4 = lista_numeros[1:4]
print(lista_numeros_del_2_al_4)

numeros_en_posiciones_pares = lista_numeros[::2]
print(numeros_en_posiciones_pares)

lista_reverse = lista_numeros[::-1]
print(lista_reverse)

# Conjuntos
lista = [1, 2, 2, 2, 3, 3, 4, 5, 6, 6, 6, 7, 8]

conjunto_1 = set(lista)
# conjunto_1 = {}
conjunto_2 = set([1, 4, 9, 10])

print(conjunto_1)

print(conjunto_1.intersection(conjunto_2))
print(conjunto_1.union(conjunto_2))
print(conjunto_1.difference(conjunto_2))
print(conjunto_1.symmetric_difference(conjunto_2))

# Tuplas
una_tupla = (1, 2, 3, 4)
print(una_tupla)
# una_tupla[1] = 10


# Desempaquetado (unpacking)
numero_telefono = ('+34', 666777888)
# prefijo = numero_telefono[0]
# numero = numero_telefono[1]

prefijo, numero = numero_telefono
print(prefijo)
print(numero)

n1, n2, *resto = una_tupla
print(resto)

n1, *resto, nn = una_tupla
print(resto)


# Mutables
persona_1 = {
  "nombre": "JSON",
  "apellido": "Statham"
}

credenciales_1 = {
  "usuario": "json.statham@gmail.com",
  "password": "12345"
}
# persona_2 = persona_1
# persona_2["nombre"] = "YAML"

persona_2 = {**persona_1}
persona_2["nombre"] = "YAML"

print(persona_2)
print(persona_1)

usuario_completo = {**persona_1, **credenciales_1}
print(usuario_completo)

# lista_2 = lista
lista_2 = [*lista]
lista_2[0] = 20

lista_3 = [*lista, *lista_numeros]
print(lista_3)