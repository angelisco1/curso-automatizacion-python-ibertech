# import constantes
# from constantes import url, api_key as ak
import constantes as ct

# import utils.traducciones
# import utils.traducciones as tr

# from utils.validaciones import solo_mayusculas

import utils

def get_datos(api_url, key):
  print(f"Petición a {api_url} con la api key {key}")

# get_datos(constantes.url, constantes.api_key)
get_datos(ct.url, ct.api_key)

# print(url)

# api_key = "kaosdojaiodkals"
# print(api_key)
# print(ak)


# print(utils.traducciones.traducir("hola", "it"))
# print(tr.traducir("hola", "it"))

# print(solo_mayusculas("HoLA"))

print(utils.validaciones.es_mayor(1, 3))
print(utils.solo_minusculas("un texto cualquiera"))