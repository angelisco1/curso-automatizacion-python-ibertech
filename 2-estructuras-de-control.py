for i in range(5):
  print(i)

lista = [1, 3, 4, 10]
for n in lista:
  print(n)

for pos, num in enumerate(lista):
  # print(f"Pos: {pos} - Num: {num}")
  if not pos % 2:
    print(num)

sugus = {
  "azul": "piña",
  "rojo": "fresa",
  "amarillo": "limón",
  "naranja": "naranja"
}

for sabor in sugus.values():
  print(sabor)

for color in sugus.keys():
  print(color)

for color, sabor in sugus.items():
  print(f"Color: {color}, Sabor: {sabor}")


sabor_buscado = "mango"
for sabor in sugus.values():
  if sabor == sabor_buscado:
    print(f"Si que existe el sabor {sabor_buscado}")
    break
else:
  print(f"No existe el sabor {sabor_buscado}")