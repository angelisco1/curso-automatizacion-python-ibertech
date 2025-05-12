from abc import ABC, abstractmethod

class Persona:
  # atributo de clase
  num_cabezas = 1

  def __init__(self, nombre, apellidos, edad, esta_trabajando, dni):
    # atributos de instancia
    self._nombre = nombre
    self._apellidos = apellidos
    self._edad = edad
    self._esta_trabajando = esta_trabajando
    self.dni = dni

  # método de instancia
  def get_nombre_completo(self):
    return f"{self._nombre} {self._apellidos}"

  def __str__(self):
    return f"Persona(nombre={self._nombre}, apellidos={self._apellidos}, edad={self._edad}, esta_trabajando={self._esta_trabajando})"

  def __repr__(self):
    return f"Persona(nombre={self._nombre}, apellidos={self._apellidos}, edad={self._edad}, esta_trabajando={self._esta_trabajando})"

  def __eq__(self, persona):
    return self.dni == persona.dni

  def __ne__(self, persona):
    return not self.__eq__(persona)

  def __lt__(self, persona):
    return self._edad < persona._edad

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

  # Otra forma de usar getters y setters
  def get_apellidos(self):
    return self._apellidos

  def set_apellidos(self, nuevos_apellidos):
    # print('Pasa por el setter')
    self._apellidos = nuevos_apellidos

  apellidos = property(get_apellidos, set_apellidos)


charly = Persona("Charly", "Falco", 52, True, "00000000T")
octavia = Persona("Octavia", "Blake", 43, True, "00000001T")

print(charly)
print(charly.nombre)
print(charly.get_nombre_completo())

charly.apellidos = "Falco García"
print(charly.apellidos)

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

print(charly == octavia)
mike = charly
print(mike == charly)

charly2 = Persona("Charly", "Falco", 42, True, "00000000T")
print(charly == charly2)

charly3 = Persona("Charly", "Falco", 42, True, "00000002Z")
print(charly == charly3)

print(charly < octavia)


# Herencia
class Leccion:

  def __init__(self, titulo, duracion):
    self.titulo = titulo
    self.duracion = duracion

  def __str__(self):
    return f"\n- Lección {self.titulo} (Duración: {self.duracion})"

  def metodo1(self):
    # print("metodo1 en Leccion")
    raise NotImplementedError("Tienes que implementar el metodo1")

class LeccionTexto(Leccion):

  def __init__(self, titulo, duracion, contenido):
    super().__init__(titulo, duracion)
    self.contenido = contenido

  def __str__(self):
    leccion_str = super().__str__()
    return f"{leccion_str}\n\n\t{self.contenido}"

  def metodo1(self):
    print("metodo1 en LeccionTexto")


class LeccionMultimedia(Leccion):

  def __init__(self, titulo, duracion, url):
    super().__init__(titulo, duracion)
    self.url = url

  def __str__(self):
    leccion_str = super().__str__()
    return f"{leccion_str}\n\n\tAccede a {self.url}"

  def metodo1(self):
    print("metodo1 en LeccionMultimedia")


introduccion = LeccionTexto("Introducción", 10, "Esta es la introducción a ...")
print(introduccion)

instalacion = LeccionMultimedia("Instalación", 20, "http://curso.com/instalacion.mp4")
print(instalacion)

introduccion.metodo1()
instalacion.metodo1()



# Clases abstractas
class Leccion2(ABC):

  def __init__(self, titulo, duracion):
    self.titulo = titulo
    self.duracion = duracion

  def __str__(self):
    return f"\n- Lección {self.titulo} (Duración: {self.duracion})"

  @abstractmethod
  def metodo1(self):
    pass

class LeccionTexto2(Leccion2):

  def __init__(self, titulo, duracion, contenido):
    super().__init__(titulo, duracion)
    self.contenido = contenido

  def __str__(self):
    leccion_str = super().__str__()
    return f"{leccion_str}\n\n\t{self.contenido}"

  def metodo1(self):
    print("metodo1 en LeccionTexto")


class LeccionMultimedia2(Leccion2):

  def __init__(self, titulo, duracion, url):
    super().__init__(titulo, duracion)
    self.url = url

  def __str__(self):
    leccion_str = super().__str__()
    return f"{leccion_str}\n\n\tAccede a {self.url}"

  def metodo1(self):
    print("metodo1 en LeccionMultimedia")


introduccion2 = LeccionTexto2("Introducción", 10, "Esta es la introducción a ...")
instalacion2 = LeccionMultimedia2("Instalación", 20, "http://curso.com/instalacion.mp4")
introduccion2.metodo1()
instalacion2.metodo1()