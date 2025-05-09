class Persona:
  # atributo de clase
  num_cabezas = 1

  def __init__(self, nombre, apellidos, edad, esta_trabajando):
    # atributos de instancia
    self._nombre = nombre
    self._apellidos = apellidos
    self._edad = edad
    self._esta_trabajando = esta_trabajando

  # método de instancia
  def get_nombre_completo(self):
    return f"{self._nombre} {self._apellidos}"

  def __str__(self):
    return f"Persona(nombre={self._nombre}, apellidos={self._apellidos}, edad={self._edad}, esta_trabajando={self._esta_trabajando})"

  def __repr__(self):
    return f"Persona(nombre={self._nombre}, apellidos={self._apellidos}, edad={self._edad}, esta_trabajando={self._esta_trabajando})"

  # GETTERS
  @property
  def nombre(self):
    return self._nombre

  @property
  def edad(self):
    return self._edad

  # SETTERS
  @edad.setter
  def edad(self, nueva_edad):
    self._edad = nueva_edad


charly = Persona("Charly", "Falco", 42, True)
octavia = Persona("Octavia", "Blake", 43, True)

print(charly)
print(charly.nombre)
print(charly.get_nombre_completo())

print(Persona.get_nombre_completo(octavia))

print(octavia.edad)
octavia.edad += 1 # -> octavia.edad = octavia.edad + 1
print(octavia.edad)

Persona.num_cabezas = 2
print(Persona.num_cabezas)
print(octavia.num_cabezas)

lista_personas = [charly, octavia]
print(lista_personas)

print(charly._edad)