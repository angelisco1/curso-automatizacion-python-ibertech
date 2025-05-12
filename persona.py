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