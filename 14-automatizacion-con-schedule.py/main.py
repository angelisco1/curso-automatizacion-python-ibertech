import schedule
import time

class EjecucionesTarea:
  def __init__(self, tarea):
    self.num_ejecuciones = 0
    self.tarea = tarea

  def ejecutar_tarea(self, *args):
    self.tarea(*args)
    self.num_ejecuciones += 1

def tarea(num):
  print(f"Se ha ejecutado la tarea {str(num)}")
  # global num_ejecuciones
  # num_ejecuciones += 1

if __name__ == "__main__":

  t1 = EjecucionesTarea(tarea)

  # schedule.every(2).seconds.do(tarea, 1).tag('tarea1')
  # schedule.every().wednesday.at("09:56:00").do(tarea, 2).tag('tarea2')

  schedule.every(2).seconds.do(t1.ejecutar_tarea, 1).tag('tarea1')


  while True:
    schedule.run_pending()

    if t1.num_ejecuciones == 5:
      schedule.clear('tarea1')

    time.sleep(2)
