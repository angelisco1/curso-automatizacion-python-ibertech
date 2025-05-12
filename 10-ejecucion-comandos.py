import subprocess

resultado = subprocess.run(["echo", "Hola mundo!"], capture_output=True)
print(resultado.stdout)

resultado = subprocess.run(["echo", "Hola mundo!"], capture_output=True, text=True)
print(resultado.stdout)

resultado = subprocess.run(["ls", "-l", "/no-existe/esta_carpeta"], capture_output=True, text=True)
# print(resultado.stdout)
print(resultado.stderr)


with open("created_files/logs.txt", "w") as file:
  subprocess.run(["ls", "-l"], stdout=file)


# subprocess.run(["ffmpeg", "-i", "files/video.mp4", "-ss", "00:00:02", "-vframes", "1", "created_files/capturas/captura-1.png"])


# subprocess con Popen
subprocess.Popen(["ls", "-l"])

proceso = subprocess.Popen(["ls", "-l"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
stdout, stderr = proceso.communicate()
# print("-----")
# print("-----")
# print("-----")
# print(stdout)
# print("-----")
# print("-----")
# print("-----")


proceso_listar = subprocess.Popen(["ls", "-l"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
proceso_filtrar = subprocess.Popen(["grep", "py"], stdin=proceso_listar.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

stdout, stderr = proceso_filtrar.communicate()
print("-----")
print("-----")
print("-----")
print(stdout)
print("-----")
print("-----")
print("-----")


lista_correos = ["angel@gmail.com", "angel@patatas.es", "paco@gmail.com"]
filtrar_emails = subprocess.Popen(["grep", "gmail.com"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

stdout, stderr = filtrar_emails.communicate(input="\n".join(lista_correos))
print(stdout)