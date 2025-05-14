import pyautogui
import time


def borrar_2_imagenes_de_carpeta():
  pyautogui.moveTo(810, 1735, 2)
  pyautogui.click()

  pyautogui.keyDown("shift")

  pyautogui.moveRel(0, 20, 1)
  pyautogui.click()

  pyautogui.rightClick()

  pyautogui.moveRel(75, 92, 1)
  pyautogui.click()


def mover_archivo_entre_carpetas():
  pyautogui.moveTo(810, 1735, 2)
  pyautogui.click()

  pyautogui.keyDown("shift")

  pyautogui.moveRel(0, 20, 1)
  pyautogui.click()

  pyautogui.dragRel(710, 425, 1, button="left")


def escribir_y_guardar_en_vs_code():
  pyautogui.moveTo(1800, 1800, 1)
  pyautogui.click()

  pyautogui.hotkey("command", "a")
  pyautogui.press("backspace")

  pyautogui.write("Otro texto")

  pyautogui.hotkey("command", "s")



def escribir_y_guardar_en_vs_code_usando_imagen():
  captura_archivo = "/Users/angelisco1/Pronoide/mis-cursos/curso-ibertech-automatizacion-python/curso-automatizacion-python-ibertech/files/captura-archivo.png"

  pyautogui.moveTo(1800, 1800, 1)
  pyautogui.click()

  pyautogui.hotkey("command", "a")
  pyautogui.press("backspace")

  pyautogui.write("Otro texto")

  posicion_archivo = pyautogui.locateCenterOnScreen(captura_archivo)
  print(posicion_archivo)
  # pyautogui.moveTo(posicion_archivo)

def buscar_mariposa():
  time.sleep(3)
  captura_archivo = "/Users/angelisco1/Pronoide/mis-cursos/curso-ibertech-automatizacion-python/curso-automatizacion-python-ibertech/files/codigo.png"

  posicion_archivo = pyautogui.locateCenterOnScreen(captura_archivo)
  print(posicion_archivo)
  pyautogui.moveTo(posicion_archivo)


if __name__ == "__main__":
  # borrar_2_imagenes_de_carpeta()
  # mover_archivo_entre_carpetas()
  # escribir_y_guardar_en_vs_code()
  # escribir_y_guardar_en_vs_code_usando_imagen()
  buscar_mariposa()