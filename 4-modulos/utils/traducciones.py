traducciones = {
  "en": {
    "hola": "hello",
    "adios": "bye"
  },
  "es": {
    "hola": "hola",
    "adios": "adios"
  }
}

def traducir(texto, lang="en"):
  if lang in traducciones.keys():
    if texto in traducciones[lang].keys():
      return traducciones[lang][texto]
    else:
      return "No tenemos esa traducción"
  else:
    return "No tenemos ese idioma"


# print(__name__)

if __name__ == "__main__":
  print(traducir("adios", "en"))
  print(traducir("adios", "es"))