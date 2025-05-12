from getpass import getpass
import time
import csv
import os

# # Lectura de datos desde el terminal
# usuario = input("- Introduce tu usuario:")
# # password = input("- Introduce tu password:")
# password = getpass("- Introduce tu password:")

# print(f"Usuario: {usuario}; Password: {password}")


# r -> lectura
# rb -> lectura de archivos binarios
# w -> escritura
# wb -> escritura de archivos binarios
# a -> añadir al final


# Leer el archivo
file = open("files/archivo.txt", "r")
print(file.read())
file.close()


with open("files/archivo.txt", "r") as file:
  print(file.read())

with open("files/archivo.txt", "r") as file:
  # line = file.readline()
  # print(line)
  # line = file.readline()
  # print(line)

  for line in file:
    print(f"[+] {line}")


with open("files/archivo.txt", "r") as file:
  lineas = file.readlines()
  for line in lineas:
    print(f"[-] {line}")


# Escribir en ficheros

with open("created_files/archivo1.txt", "w") as file:
  file.write("Hola, que tal?\n")
  file.write("Muy bien, y tu??\nTambién bien\n")


# time.sleep(3)
with open("created_files/archivo1.txt", "a") as file:
  file.write("Te vienes?\n")


with open("files/archivo-a-copiar.txt", "r") as file_read, open("created_files/archivo-copiado.txt", "w") as file_write:
  for password in file_read:
    file_write.write(password)


# Trabajar con archivos CSV
path_archivo_csv = "files/apple_store.csv"

with open(path_archivo_csv, "r") as file:
  csvreader = csv.reader(file)
  for pos, fila in enumerate(csvreader):
    if pos == 10:
      break
    print(fila)

# Con DictReader
with open(path_archivo_csv, "r") as file:
  csvreader = csv.DictReader(file)
  # csvreader = list(csv.DictReader(file))

  for pos, fila in enumerate(csvreader):
    if pos == 5:
      break
    print(fila)

  print('---------')
  print('---------')
  print('---------')

  for pos, fila in enumerate(csvreader):
    if pos < 5:
      continue
    elif pos >= 5 and pos < 10:
      print(fila)
    else:
      break
    # print(fila)


class AplicacionStore:
  def __init__(self, id, name, price, rating, genre):
    self.id = id
    self.name = name
    self.price = price
    self.rating = rating
    self.genre = genre

  def __str__(self):
    return f"App (name: {self.name}, price: {self.price})"


aplicaciones = []

with open(path_archivo_csv, "r") as file:
  csvreader = csv.DictReader(file)

  for pos, fila in enumerate(csvreader):
    id, track_name, size, price, r1, r2, user_rating, r3, prime_genre, *_ = fila.values()
    aplicaciones.append(AplicacionStore(id, track_name, price, user_rating, prime_genre))

print(len(aplicaciones))
print(aplicaciones[1])


# Escritura en CSV

ofertas = [
  {
    "id": "1234abc",
    "titulo": "Desarrollador Full Stack con Ruby",
    "empresa": "Empresa 1",
    "lugar_de_trabajo": "remoto",
    "salario": 30000
  },
  {
    "id": "1234def",
    "titulo": "Programador blockchain",
    "empresa": "Empresa 2",
    "lugar_de_trabajo": "Madrid",
    "salario": 45000
  },
  {
    "id": "0987abc",
    "titulo": "Desarrollador junior Java",
    "empresa": "Empresa 1",
    "lugar_de_trabajo": "Valencia",
    "salario": 25000
  }
]

with open("created_files/ofertas.csv", "w") as file:
  writer = csv.writer(file)

  writer.writerow(ofertas[0].keys())

  for oferta in ofertas:
    # writer.writerow((oferta["id"], oferta["titulo"], oferta["empresa"], oferta["lugar_de_trabajo"], oferta["salario"]))
    writer.writerow(oferta.values())



with open("created_files/ofertas_2.csv", "w") as file:
  writer = csv.DictWriter(file, fieldnames=ofertas[0].keys(), delimiter=";")

  # writer.writerow(ofertas[0].keys())
  writer.writeheader()

  for oferta in ofertas:
    writer.writerow(oferta)


# Módulo OS
print(os.getcwd())

with os.scandir(os.getcwd()) as ficheros:
  for fichero in ficheros:
    # print(f"{fichero.name} - {fichero.path} - dir? {fichero.is_dir()}")
    print(f"{fichero.name} - dir? {fichero.is_dir()}")

with os.scandir(f"{os.getcwd()}/files") as ficheros:
  for fichero in ficheros:
    # print(f"{fichero.name} - {fichero.path} - dir? {fichero.is_dir()}")
    # print(f"{fichero.name} - dir? {fichero.is_dir()}")
    if fichero.name == "mi-carpeta":
      print("La carpeta ya está creada")
      break
  else:
    print("Creamos la carpeta")
    os.makedirs(f"{os.getcwd()}/files/mi-carpeta")

  # if not "mi-carpeta" in [fichero.name for fichero in ficheros]:
