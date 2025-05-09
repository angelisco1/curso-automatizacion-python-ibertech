# List comprehension
nums = [1, 2, 3, 4, 5]

doble_nums = []
for num in nums:
  doble_nums.append(num * 2)

print(doble_nums)

doble_nums_comprehension = [num * 2 for num in nums]
print(doble_nums_comprehension)

doble_de_numeros_pares = [num * 2 for num in nums if num % 2 == 0]
print(doble_de_numeros_pares)

doble_de_numeros_en_posiciones_pares = [num * 2 for pos, num in enumerate(nums) if pos % 2 == 0]
print(doble_de_numeros_en_posiciones_pares)

# Ejercicio:
lemas_got = ["Un Lanister siempre paga sus deudas", "Winter is coming"]

lemas_got_minusculas = [lema.lower() for lema in lemas_got]
# lemas_got_minusculas = ["un lanister siempre paga sus deudas", "winter is coming"]
print(lemas_got_minusculas)

resultado_combinaciones = []
for i in range(3):
  for l in ["a", "b", "c"]:
    resultado_combinaciones.append((i, l))

print(resultado_combinaciones)

resultado_combinaciones_comprehension = [(i, l) for i in range(3) for l in ["a", "b", "c"] if l != "b"]
print(resultado_combinaciones_comprehension)


# Dictionary comprehension
lema = "winter is coming winter is winter"
# ["winter", "is", "coming", "winter", "is", "winter"] -> set -> ["winter", "is", "coming"]
# resultado -> {winter: 6, is: 2, coming: 6}

long_palabras_lema = {palabra: len(palabra) for palabra in lema.split(' ')}
print(long_palabras_lema)

count_palabras_en_el_lema = {palabra: lema.count(palabra) for palabra in set(lema.split(' '))}
print(count_palabras_en_el_lema)

# Set comprehension
count_palabras_en_el_lema_set = {lema.count(palabra) for palabra in set(lema.split(' '))}
print(count_palabras_en_el_lema_set)