class Libro:
  def __init__(self, titulo, imagen_url, precio, puntuacion):
    self.titulo = titulo
    self.imagen_url = imagen_url
    self.precio = precio
    self.puntuacion = puntuacion

  def __str__(self):
    return f"Libro( titulo={self.titulo}, imagen_url={self.imagen_url}, precio={self.precio}, puntuacion={self.puntuacion} )"

  def __repr__(self):
    return f"Libro( titulo={self.titulo}, imagen_url={self.imagen_url}, precio={self.precio}, puntuacion={self.puntuacion} )"